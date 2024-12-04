<!DOCTYPE html>  <!-- Headers already sent error fix: Put PHP BEFORE HTML declaration! -->
<html lang=en>
	<head>
		<title>Register Page - Website ni Domingo</title>
		<meta charset=utf-8>
		<link rel="stylesheet" type="text/css" href="css/design.css">
		<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
		<script src="js/bootstrap.bundle.min.js"></script>
	</head>
	<body class="register-bg-pattern";>
		<div id="container">
		<?php include'nav_register.php';?> <!-- DIFFERENT NAV BAR NOW BABY -->
		<h1 class="register-header";>Register a New Account</h1>
		<?php 
			if($_SERVER['REQUEST_METHOD'] == 'POST') {  // If the BUTTON is pressed...
				$errors = []; // Initialize error array
				// Does FIRST NAME have content?
				if(empty($_POST['fname'])) {
					$errors[] = 'Please enter your first name.';
				}else{
					$fn = trim($_POST['fname']);
				}
				// Does LAST NAME have content?
				if(empty($_POST['lname'])) {
					$errors[] = 'Please enter your last name.';
				}else{
					$ln = trim($_POST['lname']);
				}
				// Does EMAIL have content?
				if(empty($_POST['email'])) {
					$errors[] = 'Please enter your email address.';
				}else{
					$e = trim($_POST['email']);
				}
				// Is PASSWORD1 and PASSWORD2 the SAME?
				if(!empty($_POST['psword1'])) {
					if($_POST['psword1'] != $_POST['psword2']) { // check if PASSWORDS are the SAME
						$errors[] = 'Your passwords don\'t match. Dummy >:('; 
					}else{ 
						// Credits: Shahzeb Ahmed (Cloudways)
						$unencrypted_password = trim($_POST['psword1']);  # Store initial password as an unencrypted password
						$hash = password_hash($unencrypted_password, PASSWORD_DEFAULT);  # Create a hash version of unencrypted password to be encrypted, store into '$hash' variable, and become new replacement for '$p' variable for password for later query in '$q' variable
						// Password is encrypted now, but still no system to verify if unencrypted password and encrypted password are the same...
					}
				}else{ // If PASSWORD is EMPTY
					$errors[] = 'Please enter your password.';
				}
				// NO ERRORS (ALL textboxes HAVE content)
				if(empty($errors)) {
					// Register the user in the database...
					require'mysqli_connect.php'; // Connect to the database.
					// Make the query:
					$q = "INSERT INTO users VALUES (NULL, '$fn', '$ln', '$e', '$hash', NOW())";	// The password ($p) is NOT encrypted. Find a way to secure this password
					$result = @mysqli_query ($dbcon, $q); // Run the query.
					if ($result) { // If it ran OK.
						header ("Location: http://localhost/domingo/register-thanks.php"); 
						exit();	
					}else{ // If it did not run OK.
						// Public message:
						echo '<h2>System Error</h2>
						<p class="error">You could not be registered due to a system error. We apologize for any inconvenience.</p>'; 
						// Debugging message:
						echo '<p>' . mysqli_error($dbcon) . '</p>';
					}
						mysqli_close($dbcon); // Close the database connection.
						// Include the footer and quit the script:
						include'footer.php';
								exit();

							}else{ // There is an ERROR :(
								echo '<h2 class="error-header">Oops! There\'s been an <u>error</u>!</h2>
								<p class="error">The following error(s) occurred:<br />
								';
								foreach($errors as $msg) {
									echo "→ $msg<br />"; // Use DOUBLE QUOTES
								}
									echo '</p><h4 class="error-footer">Please try again or whatever :3</h4><br /><br />';
							}
						}
				?>
			<div id="content">
				<br />
				<br />
				<br />
				<form action="register-page.php" method="post"> 
					<p>
						<label class="register-label" for="fname">First Name: &nbsp; </label>
						<input type="text" class="fname" name="fname" size="30" maxlength="40" value="<?php if (isset($_POST['fname'])) echo $_POST['fname']?>">
					</p>
					<p>
						<label class="register-label" for="lname">Last Name: &nbsp; </label>
						<input type="text" class="lname" name="lname" size="30" maxlength="40" value="<?php if (isset($_POST['lname'])) echo $_POST['lname']?>">
					</p>
					<p>
						<label class="register-label" for="email">Email Address: &nbsp; </label>
						<input type="email" class="email" name="email" size="30" maxlength="50" value="<?php if (isset($_POST['email'])) echo $_POST['email']?>">
					</p>
					<p>
						<label class="register-label" for="psword1">Password: &nbsp; </label>
						<input type="password" class="psword1" name="psword1" size="30" maxlength="40" value="<?php if (isset($_POST['psword1'])) echo $_POST['psword1']?>">
					</p>
					<p>
						<label class="register-label" for="psword2">Confirm Password: &nbsp; </label>
						<input type="password" class="psword2" name="psword2" size="30" maxlength="40" value="<?php if (isset($_POST['psword2'])) echo $_POST['psword2']?>">
					</p>
					<p><input type="submit" class="register-submit" name="submit" value="Register!"></p>
					</form>
			</div>
		<?php include'footer.php';?>
		</div>
	</body>
</html>