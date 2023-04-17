import "./bottomReaction.css";
import { useEffect, useRef, useState } from "react";

export default function BottomReaction({ target, chat }) {
	const [msg, setMsg] = useState(null);
	useEffect(() => {
		setMsg(document.getElementById(target));
		if (msg) {
			let reactionShowButton = document.getElementById(`${target}sh`);
			msg.addEventListener("mouseover", () => {
				reactionShowButton.style.opacity = "1";
			});
			msg.addEventListener("mouseout", () => {
				reactionShowButton.style.opacity = "0";
			});
		}
	}, [msg]);
	const PF = process.env.REACT_APP_PUBLIC_FOLDER;
	const reactions = [
		"drink",
		"heart-eye",
		"cake",
		"like",
		"vomit",
		"angry",
		"cry",
		"heart",
	];
	const showChangedReaction = (e) => {
		// if (chat) {
		let id = e.target.id.slice(0, -2);
		let button = document.getElementById(`${id}Btn`);
		for (let i in reactions) {
			let reaction = button.children[i].children[0];
			if (e.target.src == reaction.src) {
				reaction.parentElement.style.display =
					reaction.parentElement.style.display === "flex" ? "none" : "flex";
			}
		}
		// }
	};
	const handleReaction = (x) => {
		if (chat) {
			let bottomReactionButton = document.getElementsByClassName(
				"bottomReactionButton"
			);
			for (let i = 0; i < bottomReactionButton.length; i++) {
				if (bottomReactionButton[i] != x.target) {
					bottomReactionButton[i].style.display = "none";
				} else {
					bottomReactionButton[i].style.display = "block";
				}
			}
		}
	};

	return (
		<>
			<div className="postBottomLeft">
				<div className="reactionShow" id={`${target}sh`}>
					{reactions.map((r) => (
						<img
							id={`${target}ic`}
							src={PF + `emojis/${r}.gif`}
							onClick={(event) => showChangedReaction(event)}
							className="reactIconShow"></img>
					))}
				</div>
				<span id={`${target}Btn`} className="bottomReactionButtonsContainer">
					{reactions.map((r) => (
						<div className="bottomReactionButton">
							<img src={PF + `emojis/${r}.gif`} className="reactIcon"></img>
							<span className="postLikeCounter">1</span>
						</div>
					))}
				</span>
			</div>
		</>
	);
}
