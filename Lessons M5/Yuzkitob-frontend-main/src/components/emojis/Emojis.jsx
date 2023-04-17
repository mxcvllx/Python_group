import { SentimentSatisfiedRounded, Search } from "@mui/icons-material";
import emoji from "node-emoji";
import { useEffect, useState } from "react";
import "./emojis.css";
import fetchGifs from "fetch-gifs";

export default function Emojis({ setChangedGif, setChangedStiker, target }) {
	const PF = process.env.REACT_APP_PUBLIC_FOLDER;
	const [gifsAll, setGifsAll] = useState([]);
	const [searchInput, setSearchInut] = useState("hello");
	const [emojis, setEmojis] = useState([]);
	const [file, setFile] = useState(null);
	let stikerLenght = 5;
	let stikers = [];

	for (let i = 0; i < stikerLenght; i++) {
		stikers.push(PF + "/stikers/" + i + ".png");
	}
	// target &&
	// 	target.addEventListener("input", (e) => {
	// 		console.log(e);
	// 	});

	function openTabs(evt, tabId) {
		let tabcontent = document.getElementsByClassName("tabContentItem");
		for (let i = 0; i < tabcontent.length; i++)
			tabcontent[i].classList.add("d-none");
		let tablinks = document.getElementsByClassName("tabsItem");
		for (let i = 0; i < tablinks.length; i++)
			tablinks[i].classList.remove("active");
		evt.target.classList.add("active");
		document.getElementById(tabId).classList.remove("d-none");
	}

	const handleSearch = (e) => {
		setSearchInut(e.target.value);
	};
	useEffect(() => {
		if (!searchInput || searchInput == "hello") {
			setEmojis(emoji.emoji);
		} else {
			let emojilar = [];
			for (let i in emoji.emoji) {
				if (i.includes(searchInput)) {
					emojilar.push(emoji.emoji[i]);
				}
			}
			setEmojis(emojilar);
		}
	}, [searchInput]);

	useEffect(() => {
		const getGifs = async () => {
			try {
				let res = await fetchGifs(searchInput);
				res = res["data"].map((gif) => gif.medium);
				setGifsAll(res);
			} catch (error) {}
		};
		getGifs();
	}, [searchInput]);
	const emojiToInput = (e) => {
		target.value += e.target.innerHTML;
		target.focus();
	};

	return (
		<div className="emojis">
			<div
				className="emojisAllContainer d-none"
				onMouseLeave={(e) =>
					document
						.getElementById("emojiButton")
						.previousSibling.classList.add("d-none")
				}>
				<div className="tabs">
					<ul className="tabsUl">
						<li
							onClick={(event) => openTabs(event, "emoji")}
							className="tabsItem">
							Emoji
						</li>
						<li
							onClick={(event) => openTabs(event, "gifs")}
							className="tabsItem">
							Gifs
						</li>
						<li
							onClick={(event) => openTabs(event, "stikers")}
							className="tabsItem">
							Stikers
						</li>
					</ul>
				</div>
				<div className="tabContents">
					<div id="emoji" className="tabContentItem active">
						{emojis &&
							Object.keys(emojis).map((value, index) => (
								<button
									onClick={(e) => emojiToInput(e)}
									className="emojiItem"
									key={index}>
									{emojis[value]}
								</button>
							))}
					</div>
					<div id="gifs" className="tabContentItem d-none">
						{gifsAll.map((value, i) => (
							<img
								draggable="false"
								src={gifsAll[i]}
								className="gifsItem"
								key={i}
								onClick={(e) => setChangedGif(e.target.src)}></img>
						))}
					</div>
					<div id="stikers" className="tabContentItem d-none">
						{stikers.map((value, i) => (
							<img
								draggable="false"
								src={value}
								className="gifsItem"
								key={i}
								onClick={(e) => setChangedStiker(e.target.src)}></img>
						))}
					</div>
				</div>
				<div className="searchEmojiCont">
					<Search className="searchEmojiIcon"></Search>
					<input
						placeholder="Search..."
						type="text"
						className="searchEmojiInput"
						onChange={(event) => handleSearch(event)}
					/>
				</div>
			</div>
			<button
				className="emojiButton"
				id="emojiButton"
				onMouseEnter={(e) =>
					document
						.getElementById("emojiButton")
						.previousSibling.classList.remove("d-none")
				}>
				<SentimentSatisfiedRounded className="emojiButtonIcon"></SentimentSatisfiedRounded>
			</button>
		</div>
	);
}
