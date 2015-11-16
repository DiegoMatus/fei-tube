function main(){
	// Initialize collapse button
	$('.button-collapse').sideNav({
			menuWidth: 240, // Default is 240
			edge: 'left', // Choose the horizontal origin
			//closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
		}
	);
	// Initialize collapsible (uncomment the line below if you use the dropdown variation)
	//$('.collapsible').collapsible();

	$('.modal-trigger').leanModal();

	/*$('#upload_form').on('submit', function(e){
		e.preventDefault();
		$.ajax({
			url : '/upload/video',
			type: 'POST',
			data: {
				video_title: $('#video_title').val(),
				video_tags: $('#video_tags').val(),
				video_description: $('#video_description').val(),
				video_path: $('#video_source').val()
			},
			success : function(data){
				alert("Tu video " + data.video_path + " se está subiendo");
			},
			error : function(error){
				console.log(error);
			}
		});
	});*/
}

$(document).on('ready', main);