import { useState, useEffect, useContext } from "react";
import Post from "../post/Post";
import Share from "../share/Share";
import "./feed.css";
import axios from "axios";
import { AuthContext } from "../../context/AuthContext";

export default function Feed({ username, explore }) {
	const [posts, setPosts] = useState([]);
	const { user } = useContext(AuthContext);

	useEffect(() => {
		const fetchPosts = async () => {
			let res = "";
			if (!explore) {
				res = username
					? await axios.get("/posts/profile/" + username)
					: await axios.get("/posts/timeline/" + user._id);
			} else {
				res = await axios.get("/posts/postsAll");
			}

			setPosts(
				res.data.sort((a, b) => {
					return new Date(b.createdAt) - new Date(a.createdAt);
				})
			);
		};
		fetchPosts();
	}, [username, user._id]);

	return (
		<div className="feed">
			<div className="feedWrapper">
				{((!explore && !username) || username == user.username) && (
					<Share></Share>
				)}
				{!posts.length && <h1 className="noPosts">Hali post joylanmagan</h1>}
				{posts.map((p) => (
					<Post key={p._id} post={p}></Post>
				))}
			</div>
		</div>
	);
}
