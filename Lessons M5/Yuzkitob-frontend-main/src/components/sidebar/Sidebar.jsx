import "./sidebar.css";
import {
	Person4Rounded,
	CabinRounded,
	CircleNotificationsRounded,
	MessageRounded,
	Explore,
	AddAPhotoRounded,
	DarkModeRounded,
	LightModeRounded,
	FontDownloadRounded,
	ExitToApp,
} from "@mui/icons-material";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthContext";
// import CloseFriend from "../closeFriend/CloseFriend";

export default function Sidebar() {
	let theme = localStorage.getItem("theme") || "dark-version";
	const { user } = useContext(AuthContext);

	const clearAll = () => {
		localStorage.removeItem("user");
	};
	const changeTheme = () => {
		if (theme == "dark-version") {
			localStorage.setItem("theme", "light-version");
		} else {
			localStorage.setItem("theme", "dark-version");
		}
		window.location.reload();
	};
	return (
		<div className="sidebar">
			<div className="sidebarWrapper">
				<a className="sidebarLink" href="/">
					<span className="sidebarLogo sidebarnotResponsiveLogo">Yuzkitob</span>
					<span className="sidebarLogo sidebarResponsiveLogo">Yk</span>
				</a>
				<ul className="sidebarList">
					<a href="/" className="sidebarLink">
						<li className="sidebarListItem">
							<CabinRounded className="sidebarIcon"></CabinRounded>
							<span className="sidebarListItemText">Bosh sahifa</span>
						</li>
					</a>
					<a href="/explore" className="sidebarLink">
						<li className="sidebarListItem">
							<Explore className="sidebarIcon"></Explore>
							<span className="sidebarListItemText">Boshqalar</span>
						</li>
					</a>
					<a href="/messanger" className="sidebarLink">
						<li className="sidebarListItem sidebarListItemBadge">
							<MessageRounded className="sidebarIcon"></MessageRounded>
							<span className="sidebarListItemText">Yozishmalar</span>
							<span className="sidebarNotificationBadge">0</span>
						</li>
					</a>
					<li className="sidebarListItem sidebarListItemBadge">
						<CircleNotificationsRounded className="sidebarIcon"></CircleNotificationsRounded>
						<span className="sidebarListItemText">Bildirishnoma</span>
						<span className="sidebarNotificationBadge">0</span>
					</li>
					<li className="sidebarListItem">
						<AddAPhotoRounded className="sidebarIcon"></AddAPhotoRounded>
						<span className="sidebarListItemText">Post qo'shish</span>
					</li>
					<a className="sidebarLink" href={`/profile/${user.username}`}>
						<li className="sidebarListItem">
							<Person4Rounded className="sidebarIcon"></Person4Rounded>
							<span className="sidebarListItemText">Sozlamalar</span>
						</li>
					</a>
					<a onClick={changeTheme} className="sidebarLink">
						<li className="sidebarListItem">
							{theme == "dark-version" ? (
								<>
									<LightModeRounded className="sidebarIcon"></LightModeRounded>
									<span className="sidebarListItemText">Light</span>
								</>
							) : (
								<>
									<DarkModeRounded className="sidebarIcon"></DarkModeRounded>
									<span className="sidebarListItemText">Dark</span>
								</>
							)}
						</li>
					</a>
					<a onClick={changeTheme} className="sidebarLink">
						<li className="sidebarListItem exitApp" onClick={clearAll}>
							<ExitToApp className="sidebarIcon"></ExitToApp>
							<span className="sidebarListItemText">Chiqish</span>
						</li>
					</a>
				</ul>
			</div>
		</div>
	);
}
