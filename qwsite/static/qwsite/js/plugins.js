$(document).ready(function() {

  /* Bar creation + animations */
  $('.barres li').each(function() {
  	var pourcentage = $(this).attr('data-skills');
  	$(this).append($("<span></span>").animate({
  		width : ''+ pourcentage +'%' }, 2000));	
  });



  /* ContactForm SlideDown */
  var documentBody = (($.browser.chrome)||($.browser.safari)) ? document.body : document.documentElement;
  $('.toContactform').click(function () {
	  $('.contactform').slideDown('slow');
	  window.scrollTo(0,0);
  });

  /* ContactForm Close */
  var documentBody = (($.browser.chrome)||($.browser.safari)) ? document.body : document.documentElement;
  $('.fa-times').click(function () {
	  $('.contactform').slideUp('slow');
  });

  /* Experience Scroll */
  var documentBody = (($.browser.chrome)||($.browser.safari)) ? document.body : document.documentElement;
  $('.exp.fa-angle-right').click(function () {
	  $('.moreExperience').slideToggle('slow');
	  $(this).toggleClass('fa-angle-right');
	  $(this).toggleClass('fa-angle-down');
  });

  /* Education Scroll */
  var documentBody = (($.browser.chrome)||($.browser.safari)) ? document.body : document.documentElement;
  $('.ed.fa-angle-right').click(function () {
	  $('.moreEducation').slideToggle('slow');
	  $(this).toggleClass('fa-angle-right');
	  $(this).toggleClass('fa-angle-down');
  });

  /* Training Scroll */
  var documentBody = (($.browser.chrome)||($.browser.safari)) ? document.body : document.documentElement;
  $('.tr.fa-angle-right').click(function () {
	  $('.moreTraining').slideToggle('slow');
	  $(this).toggleClass('fa-angle-right');
	  $(this).toggleClass('fa-angle-down');
  });

}); // document.ready End