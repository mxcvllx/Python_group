import { useEffect, useState } from "react";
import "./chatOnline.css";
import axios from "axios";

export default function ChatOnline({ onlineUsers, conversation, currentUser }) {
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

	const onlineUsersIds = onlineUsers.map((a) => a.userId);

	return (
		<div className="chatOnlineFriend">
			<div className="chatOnlineImgContainer">
				<img
					className="chatOnlineImg"
					src={
						user?.profilePicture ? user.profilePicture : PF + "person/user.png"
					}
					alt=""
				/>
				{onlineUsersIds.includes(user?._id) && (
					<div className="chatOnlineBadge"></div>
				)}
			</div>
			<div className="chatOnlineName">
				{user?.username}
				<span className="conversationDescMessage">
					{user?.desc || "Hello World !!!"}
				</span>
			</div>
		</div>
	);
}
