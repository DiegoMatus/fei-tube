var socket = io.connect('http://localhost:9998', { 'forceNew': true });

socket.on('messages', function(data){
	render(data);
})

function render(data){
	var html = `<img class="col s4 m2 responsive-img circle" src="${data.profile_picture}" alt="">
				<div class="col s8 m10">
					<div class="row">
						<p class="col s12 m4">${data.username}</p>
						<p class="col s12 m8">Publicado el ${data.published}</p>
					</div>
				</div>
				<blockquote class="comment col s12">
					${data.comment}
				</blockquote>`;

	var parentGuest = document.getElementById("messages"); 
	var childGuest = document.createElement("li"); 
	childGuest.class = "row section"; 
	childGuest.innerHTML = html; 
	if (data.username != undefined) {
		parentGuest.parentNode.appendChild(childGuest);
	}else{
		alert(data.comment);
	};
		document.getElementById('comment_body').value = '';
	//document.getElementById('messages').parentNode.appendChild(html);
}

 		
$('#comment_form').on('submit', function(e){
	var data = {
		username: document.getElementById('user_picture').getAttribute('alt'),
		video: document.getElementById('video-container').getAttribute('name'),
		comment: document.getElementById('comment_body').value
	};
	socket.emit('new-message', data);
	return false;
	
});



$('.modal-trigger').leanModal();

// Initialize collapse button
$('.button-collapse').sideNav({
		menuWidth: 240, // Default is 240
		edge: 'left', // Choose the horizontal origin
		//closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
	}
);

!function(d,s,id){
	var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';
	if(!d.getElementById(id)){
		js=d.createElement(s);
		js.id=id;
		js.src=p+"://platform.twitter.com/widgets.js";
		fjs.parentNode.insertBefore(js,fjs);
	}
}(document,"script","twitter-wjs");

//////////////////////////////////////////////////////////////////////////////////////////////


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


/*$('#search_form').on('submit', function(e){
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
