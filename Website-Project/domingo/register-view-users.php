<!DOCTYPE html>
<html lang=en>
	<head>
		<title>Registered Users - Website ni Domingo</title>
		<meta charset=utf-8>
		<link rel="stylesheet" type="text/css" href="css/design.css">
		<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
		<script src="js/bootstrap.bundle.min.js"></script>
	</head>
	<body class="view-users-bg-pattern";>
		<div id='container'>
		<?php include'nav_register-view-users.php';?>
		<br /> 
		<br />
		<h1 class="main-users-header">All Registered Users in MD Gear</h1>
		<br />
			<div id='content'>
				<h2 class="view-users-header" title="IT'S TRUE!!! PROMISE!!">List Of (Cool) People in MD Gear</h2>
				<p>
					<?php
						// Require db connection
						require("mysqli_connect.php");
						// Query to get data from db
						$q = "SELECT CONCAT(lname, ', ', fname) AS fullname, email, DATE_FORMAT(registration_date, '%M %d, %Y') AS regdat, user_id FROM users ORDER BY user_id ASC";
						$result = @mysqli_query($dbcon, $q);
						if($result) { // If query is successful
							echo '<table>
							<tr>
							<center>
							<strong>
							<th>Name</th>
							<th>Email Address</th>
							<th>Register Date</th>
							<th>Actions</th>
							</strong>
							</center>
							</tr>';
							while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								echo '<tr>
								<td>'.$row['fullname'].'</td>
								<td>'.$row['email'].'</td>
								<td>'.$row['regdat'].'</td>
								<td>
								<a class="btn_edit" href="edit_user.php?id='.$row['user_id'].'" title="Edit!"><i class="fa fa-edit"></i></a>
								&nbsp
								<a class="btn_delete" href="delete_user.php?id='.$row['user_id'].'" title="Delete..."><i class="fa fa-trash"></i></a>
								</td>
								</tr>';
							}
							echo '</table>';
							mysqli_free_result($result);
						}else{ // If query is not successful
							echo '<p class="error";>>> Oops, sorry! The current registered users could not be retrieved. Please contact the system administrator, kthxbye!!</p>';
						}
						mysqli_close($dbcon);
					?>
					<br />
					<br />
				</p>
			</div>
		<?php include'footer.php';?>
		</div>
	</body>
</html>