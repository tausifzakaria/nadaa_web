function sendEmail(subject, ctaLocation, body) {
	Email.send({
	Host: "smtp.gmail.com",
	Username : "urbanplace0203@gmail.com",
	Password : "UrbanPlace@04",
	To : 'nikunj.0407@gmail.com',
	From : "urbanplace0203@gmail.com",
	Subject : subject,
	Body : body,
	}).then(
		message => alert("mail sent successfully")
	);
}