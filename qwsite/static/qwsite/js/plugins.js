$(document).ready(function() {

  /* Bar creation + animations */
  $('.barres li').each(function() {
  	var pourcentage = $(this).attr('data-skills');
  	$(this).append($("<span></span>").animate({
  		width : ''+ pourcentage +'%' }, 2000));	
  });



  /* Afficher le formulaire de contact en scrollant */
  var documentBody = (($.browser.chrome)||($.browser.safari)) ? document.body : document.documentElement;
  $('.toContactform').click(function () {
  	$('.contactform').slideDown('slow');
  	window.scrollTo(0,0);
  });


}); // document.ready End