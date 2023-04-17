import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import "./home.css";

let theme = localStorage.getItem("theme") || "dark-version";

export default function Home() {
	return (
		<div>
			<div className={`home ${theme}`}>
				<Sidebar></Sidebar>
				<Feed></Feed>
				<Rightbar></Rightbar>
			</div>
		</div>
	);
}
