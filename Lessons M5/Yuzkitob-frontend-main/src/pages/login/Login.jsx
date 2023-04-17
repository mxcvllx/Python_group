import { useContext, useRef } from "react";
import "./login.css";
import { loginCall } from "../../apiCalls";
import { AuthContext } from "../../context/AuthContext";
import { CircularProgress } from "@mui/material";
import { Link } from "react-router-dom";

export default function Login() {
	const email = useRef();
	const password = useRef();

	const { user, isFetching, error, dispatch } = useContext(AuthContext);
	const handleClick = (e) => {
		e.preventDefault();
		loginCall(
			{ email: email.current.value, password: password.current.value },
			dispatch
		);
		if (error) {
			console.log(error);
			return;
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
							placeholder="Email"
							type="email"
							className="loginInput"
							ref={email}
							required
						/>
						<input
							placeholder="Parol"
							type="password"
							className="loginInput"
							ref={password}
							minLength="6"
							required
						/>
						<button className="loginButton" disabled={isFetching}>
							{isFetching ? (
								<CircularProgress
									color="inherit"
									size="25px"></CircularProgress>
							) : (
								"Kirish"
							)}
						</button>
						<span className="loginForgot">Parolni unutdingizmi ?</span>
						<hr className="loginHr" />
						<Link to="/register">
							<button className="loginRegisterButton" disabled={isFetching}>
								{isFetching ? (
									<CircularProgress
										color="inherit"
										size="25px"></CircularProgress>
								) : (
									"Yangi akkaunt ochish"
								)}
							</button>
						</Link>
					</form>
				</div>
			</div>
		</div>
	);
}
