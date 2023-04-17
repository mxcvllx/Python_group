import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import "./profile.css";
import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router";
import { UploadFileRounded } from "@mui/icons-material";

export default function Profile() {
	const PF = process.env.REACT_APP_PUBLIC_FOLDER;
	let theme = localStorage.getItem("theme") || "dark-version";
	const [user, setUser] = useState({});
	const username = useParams().username;

	useEffect(() => {
		const fetchUser = async () => {
			const res = await axios.get(`/users?username=${username}`);
			setUser(res.data);
		};
		fetchUser();
	}, []);

	return (
		<div>
			<div className={`profile ${theme}`}>
				<Sidebar></Sidebar>
				<div className="profileRight">
					<div className="profileRightTop">
						<div className="profileCover">
							<img
								className="profileCoverImg"
								src={user.coverPicture || PF + "person/coverImg.png"}
								alt=""
							/>
							<span className="uploadCoverPic">
								<label htmlFor="coverImg">
									<UploadFileRounded className="uploadCoverPicButton"></UploadFileRounded>
									<input
										style={{ display: "none" }}
										type="file"
										id="coverImg"
									/>
								</label>
							</span>
							<span className="uploadProfilePicCont">
								<img
									className="profileUserImg"
									src={user.profilePicture || PF + "person/user.png"}
									alt=""
								/>
								<span className="uploadProfilePic">
									<label htmlFor="profileImg">
										<UploadFileRounded className="uploadProfilePicButton"></UploadFileRounded>
										<input
											type="file"
											id="profileImg"
											style={{ display: "none" }}
										/>
									</label>
								</span>
							</span>
						</div>
						<div className="profileInfo">
							<h4 className="profileInfoName">{user.username}</h4>
							<span className="profileInfoDesc">{user.desc}</span>
						</div>
					</div>
					<div className="profileRightBottom">
						<Feed username={username}></Feed>
						<Rightbar user={user}></Rightbar>
					</div>
				</div>
			</div>
		</div>
	);
}
