import "./explore.css";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";

export default function Explore() {
	const PF = process.env.REACT_APP_PUBLIC_FOLDER;
	let theme = localStorage.getItem("theme") || "dark-version";

	return (
		<div className={`explore ${theme}`}>
			<Sidebar />
			<div className="exploreRight">
				<div className="feedContainer">
					<Feed explore></Feed>
				</div>
			</div>
		</div>
	);
}
