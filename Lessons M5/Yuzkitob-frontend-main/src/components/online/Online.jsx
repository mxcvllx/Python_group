import "./online.css";

export default function Online({ user }) {
	const PF = process.env.REACT_APP_PUBLIC_FOLDER;
	return (
		<a href={`/profile/${user.username}`} className="usersLink">
			<li className="rightbarFriend">
				<div className="rightbarProfileImgContainer">
					<img
						className="rightbarProfileImg"
						src={
							user.profilePicture ? user.profilePicture : PF + "person/user.png"
						}
						alt=""
					/>
				</div>
				<span className="rightbarUsername">{user.username}</span>
			</li>
		</a>
	);
}
