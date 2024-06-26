// Task 8.2 - App Controller

class AppController {
	// Controlls the server
	static getHomepage(req, res) {
		res.status(200).send('Hello Atlas School!');
	}
}

module.exports = AppController;
