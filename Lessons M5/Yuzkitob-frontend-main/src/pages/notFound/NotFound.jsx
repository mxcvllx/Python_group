import "./notFound.css";
import Sidebar from "../../components/sidebar/Sidebar";
import { useRef } from "react";

export default function NotFound() {
	let theme = localStorage.getItem("theme") || "dark-version";
	let faces = [
		"ᕮó⏠òᕭ",
		"﴾Ȍ◡Ȍ﴿",
		"(⌾▾⌾)/",
		"ᕦ(✿◞ ✿)ᕥ",
		"﴾ȌᎲȌ﴿",
		"ᕦ🄋 !🄋 ᕥ",
		"ᕮ■ ͜ʖ■ᕭ",
		"ᕮ≋Ꮂ≋ᕭ",
	];
	let changedFace = Math.floor(Math.random() * faces.length);
	console.log(changedFace);
	return (
		<div className={`notFound ${theme}`}>
			<Sidebar></Sidebar>
			<div className="notFoundRight" id="changeFace">
				{faces[changedFace]}
			</div>
		</div>
	);
}
