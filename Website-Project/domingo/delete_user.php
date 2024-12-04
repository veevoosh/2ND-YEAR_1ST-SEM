<!DOCTYPE html>
<html lang=en>
	<head>
		<title>Delete User - Website ni Domingo</title>
		<meta charset=utf-8>
		<link rel="stylesheet" type="text/css" href="css/design.css">
		<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
		<script src="js/bootstrap.bundle.min.js"></script>
	</head>
	<body class="index-bg-pattern";>
		<div id="container">
		<?php include'nav_delete-edit.php';?>
		<center><h1 class="register-header";>Deleting an Account</h1></center>
		<br />
			<div id='content'>
				<?php
				// Checking for a valid ID number (NOT yet valid user !!)
					if(isset($_GET['id']) && (is_numeric($_GET['id']))) {
						$id = $_GET['id'];
					}elseif(isset($_POST['id']) && (is_numeric($_POST['id']))) {
						$id = $_POST['id'];
					}else{ // If NO valid ID number ... STOP script
						echo '<center>
						<h3>This page has been accessed in error lol why r u here bro??</h3>
						</center>';  // Message will SHOW up if '?id=__' is ERASED from link ... NO ID
						echo '<br />';
						echo '<center>
						<h4 class="redirect">>> Please click <a href="index.php", class="redirect-link">here</a> to <b>go back to the home page</b>!</h4>
						</center>';
						exit();
					}
					require('mysqli_connect.php');  // Default name is 'mysqli_connect.php' !!
					if($_SERVER['REQUEST_METHOD'] == 'POST') {  // User pressed YES
						if($_POST['sure'] == 'Yes') {
							$q = "DELETE FROM users WHERE user_id = $id"; // DELETE specific User !!!! [FIX LATER] !!!!
							$result = @mysqli_query($dbcon, $q);
							if(mysqli_affected_rows($dbcon) == 1) { // IF there is EXACTLY ONE deleted user
								echo '<center>
								<h3>The user is deleted successfully!! (Nice)</h3>
								</center>';
								echo '<br />';
								echo '<center>
								<h4 class="redirect">>> Please click <a href="register-view-users.php" class="redirect-link">here</a> to <b>go back to the view registered users page</b>!</h4>
								</center>';
							}else{
								echo '<center>
								<h3>The user is NOT deleted successfully... dunno why tho, but oops sorz</h3>
								</center>';
								echo '<br />';
								echo '<center>
								<h4 class="redirect">>> Please click <a href="register-view-users.php" class="redirect-link">here</a> to <b>go back to the view registered users page</b>!</h4>
								</center>';
							}
						}else{  // User pressed NO
							echo '<center>
							<h3>The user is NOT deleted. Don\'t worry, they\'re fine. <i>Settle</i>, jeez /j</h3>
							</center>';
							echo '<br />';
							echo '<center>
							<h4 class="redirect">>> Please click <a href="register-view-users.php" class="redirect-link">here</a> to <b>go back to the view registered users page</b>!</h4>
							</center>';
						} 
					}else{  // Display details of user to delete
						$q = "SELECT CONCAT(fname, ' ', lname) FROM users WHERE user_id = $id";  // 'LIMIT 1'
						$result = @mysqli_query($dbcon, $q);
						if(mysqli_num_rows($result) == 1) {
							$row = mysqli_fetch_array($result, MYSQLI_NUM);
							echo "<center>
							<h3>Are you sure you wanna delete <u>$row[0]</u>?</h3>
							</center>";
							echo '<br />';
							echo '
							<form action="delete_user.php" method="post">
							<center>
							<input id="submit-yes" type="submit" name="sure" value="Yes">
							<input id="submit-no" type="submit" name="sure" value="No">
							</center>
							<input type="hidden" name="id" value="'.$id.'">
							</form>
							';
						}else{  // NOT VALID ID. No members found.
							echo '<center>
							<h3>I DON\'T KNOW YOU who the <i>heck</i> r u ?!??!?!</h3>
							</center>';
							echo '<br />';
							echo '<center>
							<h4 class="redirect">>> Please click <a href="register-page.php" class="redirect-link">here</a> to <strong>go to the register page</strong>!</h4>
							</center>';
							echo '<br />';
							echo '<center>
							<h3>...AND PLEASE REGISTER, SO WE CAN KNOW YOU BETTER!!! JEEZ!!</h4>
							</center>';
						}
					}
					mysqli_close($dbcon);  // Safety precaution ...
				?>
			<br />
			<br />
			<br />
			<br />
			<br />
			<br />
			<br />
			<br />
			<br />
			<br />
			<br />
			<br />
			</div>
		<?php include'footer.php';?>
		</div>
	</body>
</html>