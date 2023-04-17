import "./messenger.css";
import Message from "../../components/message/Message";
import ChatOnline from "../../components/chatOnline/ChatOnline";
import {
	SendRounded,
	Search,
	SentimentSatisfiedRounded,
	AttachFileRounded,
	Cancel,
} from "@mui/icons-material";
import { useContext, useEffect, useRef, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import axios from "axios";
import Sidebar from "../../components/sidebar/Sidebar";
import { io } from "socket.io-client";
import Emojis from "../../components/emojis/Emojis";

export default function Messenger() {
	let theme = localStorage.getItem("theme") || "dark-version";
	const PF = process.env.REACT_APP_PUBLIC_FOLDER;
	const [conversations, setConversations] = useState([]);
	const [currentChat, setCurrentChat] = useState(null);
	const [messages, setMessages] = useState([]);
	const [newMessage, setNewMessage] = useState("");
	const [arrivalMessage, setArrivalMessage] = useState(null);
	const [onlineUsers, setOnlineUsers] = useState([]);
	const socket = useRef();
	const { user } = useContext(AuthContext);
	const scrollRef = useRef();
	const [file, setFile] = useState(null);
	const [changedGif, setChangedGif] = useState(null);
	const [changedStiker, setChangedStiker] = useState(null);

	useEffect(() => {
		socket.current = io("ws://localhost:8900");
		socket.current.on("getMessage", (data) => {
			setArrivalMessage({
				sender: data.senderId,
				text: data.text,
				createdAt: Date.now(),
			});
		});
	}, []);

	useEffect(() => {
		arrivalMessage &&
			currentChat?.members.includes(arrivalMessage.sender) &&
			setMessages((prev) => [...prev, arrivalMessage]);
	}, [arrivalMessage, currentChat]);

	useEffect(() => {
		socket.current.emit("addUser", user._id);
		socket.current.on("getUsers", (users) => {
			setOnlineUsers(users);
		});
	}, [user]);

	useEffect(() => {
		const getConversations = async () => {
			try {
				const res = await axios.get("/conversations/" + user._id);
				setConversations(res.data);
			} catch (err) {
				console.log(err);
			}
		};
		getConversations();
	}, [user._id]);

	useEffect(() => {
		const getMessages = async () => {
			try {
				const res = await axios.get("/messages/" + currentChat?._id);
				setMessages(res.data);
			} catch (err) {
				console.log(err);
			}
		};
		getMessages();
	}, [currentChat]);

	useEffect(() => {
		handleSubmit();
	}, [changedStiker]);

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (newMessage.trim() || file || changedGif) {
			const message = {
				sender: user._id,
				text: newMessage.trim(),
				conversationId: currentChat._id,
			};
			const receiverId = currentChat.members.find((m) => m != user._id);
			if (file) {
				const data = new FormData();
				data.append("file", file);
				try {
					const result = await axios.post("/upload", data);
					message.img = result.data;
				} catch (err) {
					console.log(err);
				}
			}
			if (changedGif) {
				try {
					console.log(changedGif);
					message.gif = changedGif;
				} catch (err) {
					console.log(err);
				}
			}
			if (changedStiker) {
				const data = new FormData();
				data.append("stiker", file);
				try {
					const result = await axios.post("/upload", data);
					message.img = result.data;
				} catch (err) {
					console.log(err);
				}
			}
			socket.current.emit("sendMessage", {
				senderId: user._id,
				receiverId: receiverId,
				text: newMessage,
				img: message.img,
				gif: message.gif,
			});
			try {
				const res = await axios.post("/messages", message);
				setMessages([...messages, res.data]);
				setNewMessage("");
				setFile(null);
				setChangedGif(null);
				setChangedStiker(null);
			} catch (err) {
				console.log(err);
			}
		}
	};

	useEffect(() => {
		scrollRef.current?.scrollIntoView({ behavior: "smooth" });
	}, [messages]);

	return (
		<div>
			<div className={`messenger ${theme}`}>
				<Sidebar></Sidebar>
				<div className="chatAllBoxContainer">
					<div className="chatBox">
						<div className="chatBoxWrapper">
							{currentChat ? (
								<div>
									<div className="chatBoxTop">
										{messages.map((m) => (
											<div ref={scrollRef}>
												<Message
													message={m}
													unique={m._id}
													own={m.sender == user._id}></Message>
											</div>
										))}
									</div>
									<div className="chatBoxBottom">
										{file && (
											<div className="shareImgContainer">
												<img
													className="shareImg"
													src={URL.createObjectURL(file)}
													alt="Image"
												/>
												<Cancel
													className="shareCancelImg"
													onClick={() => setFile(null)}></Cancel>
											</div>
										)}
										{changedGif && (
											<div className="shareImgContainer">
												<img
													className="shareImg"
													src={changedGif}
													alt="Image"
												/>
												<Cancel
													className="shareCancelImg"
													onClick={() => setChangedGif(null)}></Cancel>
											</div>
										)}
										<label htmlFor="mediaChat" className="mediaButton">
											<AttachFileRounded className="mediaButtonIcon"></AttachFileRounded>
											<img src={file} alt="" />
											<input
												type="file"
												name="mediaChat"
												id="mediaChat"
												style={{ display: "none" }}
												accept=".png,.gif,.jpg,.jpeg"
												onChange={(e) => setFile(e.target.files[0])}
											/>
										</label>
										<textarea
											className="chatMessageInput"
											name="Bu yerga yozing..."
											value={newMessage}
											onKeyPress={(e) => e.key === "Enter" && handleSubmit(e)}
											onChange={(e) => setNewMessage(e.target.value)}
											id="textAreaChat"></textarea>
										<div className="emojisButtonContainer">
											<Emojis
												setChangedGif={setChangedGif}
												setChangedStiker={setChangedStiker}
												target={document.getElementById(
													"textAreaChat"
												)}></Emojis>
										</div>
										<button className="chatSubmitButton" onClick={handleSubmit}>
											<SendRounded className="chatSubmitButtonIcon"></SendRounded>
										</button>
									</div>
								</div>
							) : (
								<span className="noConversationText">
									Yozish uchun do'stingizni tanlang
								</span>
							)}
						</div>
					</div>
					<div className="chatMenu">
						<div className="chatMenuWrapper">
							<div className="searchFriend">
								<Search className="searchIcon"></Search>
								<input
									type="text"
									placeholder="Do'stingizni qidiring"
									className="chatMenuInput"
								/>
							</div>
							{conversations.map((c) => (
								<div onClick={() => setCurrentChat(c)}>
									<ChatOnline
										onlineUsers={onlineUsers}
										conversation={c}
										currentUser={user}></ChatOnline>
								</div>
							))}
							<br />
							<br />
						</div>
					</div>
				</div>
			</div>
		</div>
	);
}
