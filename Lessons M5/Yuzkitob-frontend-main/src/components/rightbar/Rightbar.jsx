import "./rightbar.css";
import Online from "../online/Online";
import { Users } from "../../dummyData";
import { useState, useContext, useEffect } from "react";
import axios from "axios";
import { AuthContext } from "../../context/AuthContext";
import { Add, Remove } from "@mui/icons-material";

export default function Rightbar({ user }) {
	const PF = process.env.REACT_APP_PUBLIC_FOLDER;
	const [friends, setFriends] = useState([]);
	const [followers, setFollowers] = useState([]);
	const { user: currentUser, dispatch } = useContext(AuthContext);
	const [allUsers, setAllUsers] = useState([]);
	// const [followed, setFollowed] = useState(
	// 	currentUser.followings.includes(user?._id)
	// );
	let followed = currentUser.followings.includes(user?._id);

	useEffect(() => {
		const getAllUsers = async () => {
			try {
				const Users = await axios.get("/users/usersAll");
				let usersWithOutMe = Users.data.filter((u) => u._id != currentUser._id);
				setAllUsers(usersWithOutMe);
			} catch (err) {
				console.log(err);
			}
		};
		getAllUsers();
	}, [allUsers]);

	useEffect(() => {
		const getFriends = async () => {
			try {
				const friendList = await axios.get("/users/friends/" + user._id);
				const followerList = await axios.get("/users/followers/" + user._id);
				setFriends(friendList.data);
				setFollowers(followerList.data);
			} catch (err) {
				console.log(err);
			}
		};
		getFriends();
	}, [user, followers, friends]);

	const handleClick = async () => {
		try {
			if (followed) {
				await axios.put(`/users/${user._id}/unfollow`, {
					userId: currentUser._id,
				});
				dispatch({ type: "UNFOLLOW", payload: user._id });
			} else {
				await axios.put(`/users/${user._id}/follow`, {
					userId: currentUser._id,
				});
				dispatch({ type: "FOLLOW", payload: user._id });
			}
			followed = !followed;
		} catch (err) {
			console.log(err);
		}
		try {
			if (
				user.followers.includes(currentUser._id) &&
				user.followings.includes(currentUser._id)
			) {
				let result = await axios.post("/conversations", {
					senderId: currentUser._id,
					receiverId: user._id,
				});
			}
		} catch (error) {}
	};
	const HomeRightbar = () => {
		return (
			<div>
				<div className="birthdayContainer">
					<h4 className="rightbarTitle">Sizga taklif qilinadi</h4>
					<ul className="rightbarFriendList">
						{allUsers.map((u) => (
							<>
								{u.id != currentUser._id && (
									<Online key={u.id} user={u}></Online>
								)}
							</>
						))}
					</ul>
				</div>
			</div>
		);
	};

	const ProfileRightbar = () => {
		return (
			<>
				{user.username != currentUser.username && (
					<button className="rightbarFollowButton" onClick={handleClick}>
						{followed ? "Rad etish" : "Do'st bo'lish"}
						{followed ? <Remove></Remove> : <Add></Add>}
					</button>
				)}
				<h4 className="rightbarTitle">Foydalanuvchi haqida</h4>
				<div className="rightbarInfo">
					<div className="rightbarInfoItem">
						<span className="rightbarInfoKey">Shahar :</span>
						<span className="rightbarInfoValue">{user.city} </span>
					</div>
					<div className="rightbarInfoItem">
						<span className="rightbarInfoKey">Mamlakat :</span>
						<span className="rightbarInfoValue">{user.from} </span>
					</div>
					<div className="rightbarInfoItem">
						<span className="rightbarInfoKey">Telefon :</span>
						<span className="rightbarInfoValue">
							+998 (77) 777-77-77{user.phone}{" "}
						</span>
					</div>
				</div>
				<h4 className="rightbarTitle">Do'stlari</h4>
				<div className="rightbarFollowings">
					{friends.map((friend) => (
						<a
							key={friend._id}
							className="rightbarFollowingName"
							href={`/profile/` + friend.username}
							style={{ textDecoration: "none" }}>
							<div className="rightbarFollowing">
								<img
									className="rightbarFollowingImg"
									src={friend.profilePicture || PF + "person/user.png"}
									alt=""
								/>
								<span className="rightbarFollowingName">{friend.username}</span>
							</div>
						</a>
					))}
				</div>
				<br />
				<h4 className="rightbarTitle">Followers</h4>
				<div className="rightbarFollowings">
					{followers.map((follow) => (
						<a
							className="rightbarFollowingName"
							href={`/profile/` + follow.username}
							style={{ textDecoration: "none" }}>
							<div className="rightbarFollowing">
								<img
									className="rightbarFollowingImg"
									src={follow.profilePicture || PF + "person/user.png"}
									alt=""
								/>
								<span className="rightbarFollowingName">{follow.username}</span>
							</div>
						</a>
					))}
				</div>
			</>
		);
	};
	return (
		<div className="rightbar">
			<div className="rightbarWrapper">
				{user ? (
					<ProfileRightbar></ProfileRightbar>
				) : (
					<HomeRightbar></HomeRightbar>
				)}
			</div>
		</div>
	);
}
