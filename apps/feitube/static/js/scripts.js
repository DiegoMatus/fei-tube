function main(){
	// Initialize collapse button
	$('.button-collapse').sideNav({
			menuWidth: 240, // Default is 240
			edge: 'left', // Choose the horizontal origin
			closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
		}
	);
	// Initialize collapsible (uncomment the line below if you use the dropdown variation)
	//$('.collapsible').collapsible();

	$('.modal-trigger').leanModal();
}

$(document).on('ready', main);