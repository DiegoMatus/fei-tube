var socket = io.connect('http://192.168.1.69:9998', { 'forceNew': true });

socket.on('comments', function(data){
	renderComments(data);
})

socket.on('rates', function(data){
	if (data.average != true) {
		renderRates(data);
	}
});

socket.on('showToast', function(data){
	if (data.average == true) {
		Materialize.toast("You can't rate a video twice", 3000, 'rounded');
	}else{
		Materialize.toast('Thanks for rating', 3000, 'rounded');
	};
});

socket.on('refreshCommentField', function(){
	document.getElementById('comment_body').value = '';
});

function renderRates(data){
	truncated_average = Math.floor(data.average * 10) / 10;
	document.getElementById('rate_average').innerHTML = truncated_average;
}

function renderComments(data){
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
}

 		
$('#comment_form').on('submit', function(e){
	var data = {
		username: document.getElementById('user_picture').getAttribute('alt'),
		video: document.getElementById('video-container').getAttribute('name'),
		comment: document.getElementById('comment_body').value
	};
	socket.emit('new-comment', data);
	return false;	
});


$('.grade').on('click', function(e){
	var data = {
		username: document.getElementById('user_picture').getAttribute('alt'),
		video: document.getElementById('video-container').getAttribute('name'),
		rate: this.children[0].innerHTML
	};
	socket.emit('new-rate', data);
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