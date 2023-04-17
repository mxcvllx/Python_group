import { useEffect, useState } from "react";
import "./conversation.css";
import axios from "axios";

export default function Conversation({ conversation, currentUser }) {
	const [user, setUser] = useState(null);
	const PF = process.env.REACT_APP_PUBLIC_FOLDER;

	useEffect(() => {
		const friendId = conversation.members.find((m) => m !== currentUser._id);

		const getUser = async () => {
			try {
				const res = await axios("/users?userId=" + friendId);
				setUser(res.data);
			} catch (err) {
				console.log(err);
			}
		};
		getUser();
	}, [currentUser, conversation]);

	return (
		<div className="conversation">
			<img
				className="conversationImg"
				src={
					user?.profilePicture ? user.profilePicture : PF + "person/user.png"
				}
				alt=""
			/>
			<div className="rightBottom">
				<span className="conversationName">{user?.username}</span>
				<span className="conversationDescMessage">Hello how are you</span>
			</div>
		</div>
	);
}
