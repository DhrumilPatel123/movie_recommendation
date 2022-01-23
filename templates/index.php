<html>
<head></head>
<body style="background-color:#5DADE2">
<h1 style="text-align:center;font-size: 70px"><b>Movie Recommendation System</b></h1><br><br>
<center>
<form action="{{ url_for('recommed')}}" method="post">
<label style="font-size: 40px">Movie Name:</label>
<input  type="text" id="moviename" name="mname" placeholder="MovieName" height='20px' width='28px'><br><br>
<button style="background-color: lightgreen; height: 35px; width: 120px" type="submit">Search</button>
</form>
</center>
</body>
</html>
