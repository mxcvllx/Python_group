import React, { useContext } from "react";
import {
	BrowserRouter as Router,
	Switch,
	Route,
	Redirect,
} from "react-router-dom";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import Register from "./pages/register/Register";
import Profile from "./pages/profile/Profile";
import { AuthContext } from "./context/AuthContext";
import Messenger from "./pages/messenger/Messenger";
import Explore from "./pages/explore/Explore";
import NotFound from "./pages/notFound/NotFound";

function App() {
	const { user } = useContext(AuthContext);
	return (
		<Router>
			<Switch>
				<Route path="/login">{user ? <Redirect to="/" /> : <Login />}</Route>
				<Route path="/register">
					{user ? <Redirect to="/" /> : <Register />}
				</Route>
				{!user && <Login />}
				<Route exact path="/">
					{user ? <Home /> : <Login />}
				</Route>
				<Route exact path="/explore">
					{user ? <Explore /> : <Login />}
				</Route>
				<Route exact path="/messanger">
					{user ? <Messenger /> : <Login />}
				</Route>
				<Route exact path="/profile/:username">
					{user ? <Profile /> : <Login />}
				</Route>
				<Route>
					<NotFound />
				</Route>
			</Switch>
		</Router>
	);
}

export default App;
