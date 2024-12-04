<!DOCTYPE html>  <!-- Headers already sent error fix: Put PHP BEFORE HTML declaration! -->
<html lang=en>
	<head>
		<title>Login Page - Website ni Domingo</title>
		<meta charset=utf-8>
		<link rel="stylesheet" type="text/css" href="css/design.css">
		<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
		<script src="js/bootstrap.bundle.min.js"></script>
	</head>
	<body class="register-bg-pattern";>
		<div id="container">
		<?php include'nav_login.php';?>
		<h1 class="login-header";>Login to Your Account</h1>
			<div id="content">
				<br />
				<br />
				<br />
				<form action="register-page.php" method="post"> 
					<p>
						<label class="register-label" for="email">Email Address: &nbsp; </label>
						<input type="email" class="email" name="email" size="30" maxlength="50" value="<?php if (isset($_POST['email'])) echo $_POST['email']?>">
					</p>
					<p>
						<label class="register-label" for="psword1">Password: &nbsp; </label>
						<input type="password" class="psword1" name="psword1" size="30" maxlength="40" value="<?php if (isset($_POST['psword1'])) echo $_POST['psword1']?>">
					</p>
					<p><input type="submit" class="register-submit" name="submit" value="Login!"></p>
				</form>
				<br />
				<br />
				<br />
				<br />
			</div>
		<?php include'footer.php';?>
		</div>
	</body>
</html>