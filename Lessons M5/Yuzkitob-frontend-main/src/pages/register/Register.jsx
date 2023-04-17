import axios from "axios";
import { useRef } from "react";
import { useHistory } from "react-router-dom";
import "./register.css";
import { Link } from "react-router-dom";

export default function Login() {
	const username = useRef();
	const email = useRef();
	const password = useRef();
	const history = useHistory();

	const handleClick = async (e) => {
		e.preventDefault();
		const user = {
			username: username.current.value,
			email: email.current.value,
			password: password.current.value,
		};
		try {
			const res = await axios.post("/auth/register", user);
			history.push("/login");
		} catch (err) {
			console.log(err);
		}
	};

	return (
		<div className="login">
			<div className="loginWrapper">
				<div className="loginLeft">
					<h3 className="loginLogo">Yuzkitob</h3>
					<span className="loginDesc">
						Yuzkitob orqali do'stlaringiz va atrofingizdagilar bilan bog'laning
					</span>
				</div>
				<div className="loginRight">
					<form className="loginBox" onSubmit={handleClick}>
						<input
							type="text"
							placeholder="Username"
							className="loginInput"
							ref={username}
							required
						/>
						<input
							type="email"
							placeholder="Email"
							className="loginInput"
							ref={email}
							required
						/>
						<input
							type="password"
							placeholder="Parol"
							className="loginInput"
							ref={password}
							required
							minLength="6"
						/>
						<button className="loginButton" type="submit">
							Ro'yxatdan o'tish
						</button>
						<hr className="loginHr" />
						<Link to="/login">
							<button className="loginRegisterButton">
								Men ro'yxatdan o'tganman
							</button>
						</Link>
					</form>
				</div>
			</div>
		</div>
	);
}
