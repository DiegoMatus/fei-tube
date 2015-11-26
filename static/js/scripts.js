var socket = io.connect('http://localhost:9998', { 'forceNew': true });

function main(){
	socket.on('messages', function(data){
		render(data);
	})

	function render(data){
		var html = `<img class="col s4 m2 responsive-img circle" src="${data.profile_picture}" alt="">
					<div class="col s8 m10">
						<div class="row">
							<p class="col s4">${data.username}</p>
							<p class="col s8">${data.published}</p>
							<p class="col s8 m10">${data.comment}</p>
						</div>
					</div>`;

		var parentGuest = document.getElementById("messages"); 
		var childGuest = document.createElement("li"); 
		childGuest.class = "row"; 
		childGuest.innerHTML = html; 
		parentGuest.parentNode.appendChild(childGuest);
		//document.getElementById('messages').parentNode.appendChild(html);
		document.getElementById('comment_body').value = '';
	}

	 		
	$('#comment_form').on('submit', function(e){
		var data = {
			username: document.getElementById('profile').innerHTML,
			video: document.getElementById('video-container').getAttribute('name'),
			comment: document.getElementById('comment_body').value
		};
		socket.emit('new-message', data);
		return false;
		
	});

	// Initialize collapse button
	$('.button-collapse').sideNav({
			menuWidth: 240, // Default is 240
			edge: 'left', // Choose the horizontal origin
			//closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
		}
	);

	$('.modal-trigger').leanModal();
}

//////////////////////////////////////////////////////////////////////////////////////////////

$(document).on('ready', main);

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
