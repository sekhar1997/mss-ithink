/*
   
    Template Name : Rolling - Freelancer Portfolio Template
    Author : UiPasta Team
    Website : http://www.uipasta.com/
    Support : http://www.uipasta.com/support/
	
	
*/



/*
   
   Table Of Content
   
   1. Preloader
   2. Smooth Scroll
   3. Scroll Naviagation Background Change with Sticky Navigation
   4. Mobile Navigation Hide or Collapse on Click
   5. Scroll To Top
   6. Typed.js
   7. Parallax Background
   8. Portfolio Filtering
   9. Magnific Popup
  10. Testimonial Carousel/Slider
  11. Statistics Counter
  12. Google Map
 

*/

$(document).ready(function() {
    $('.circle, .circle1').removeClass('stop');     
        $('.triggerFull').click(function() {
                $('.circle, .circle1').toggleClass('stop');
        });
});


function animation(){
        one = document.getElementById('input_file')
        two = document.getElementById('myform')
		
        one.style.visibility = 'hidden'
            two.style.visibility = 'hidden'

        three = document.getElementById('analyze')
        four = document.getElementById('spinwheel')
       five = document.getElementById('typing')
       five.style.visibility = 'hidden'
       
            
            
            three.style.visibility = 'visible'
            four.style.visibility = 'visible'
    }

function animation2(){

one = document.getElementById('form2')
one.style.visibility = 'hidden'
two = document.getElementById('typingtext')
two.style.visibility = 'hidden'
   four = document.getElementById('spinwheel')
three = document.getElementById('analyze')
            
            three.style.visibility = 'visible'
           
            four.style.visibility = 'visible'
}


function animation3(){

one = document.getElementById('form3')
one.style.visibility = 'hidden'
two = document.getElementById('typingtext')
two.style.visibility = 'hidden'
   four = document.getElementById('spinwheel')
three = document.getElementById('analyze')
            
            three.style.visibility = 'visible'
           
            four.style.visibility = 'visible'
}


(function ($) {
    'use strict';

    jQuery(document).ready(function () {

        
       /* Preloader */
		
        $(window).on('load', function() {
          $('body').addClass('loaded');
        });
		
		
		
       /* Smooth Scroll */

        $('a.smoth-scroll').on("click", function (e) {
            var anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $(anchor.attr('href')).offset().top - 50
            }, 1000);
            e.preventDefault();
        });
		


       
       /* Scroll Naviagation Background Change with Sticky Navigation */
		 
        $(window).on('scroll', function () {
            if ($(window).scrollTop() > 100) {
                $('.header-top-area').addClass('navigation-background');
            } else {
                $('.header-top-area').removeClass('navigation-background');
            }
        });
		
		
		
		
       /* Mobile Navigation Hide or Collapse on Click */
		
        $(document).on('click', '.navbar-collapse.in', function (e) {
            if ($(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle') {
                $(this).collapse('hide');
            }
        });
        $('body').scrollspy({
            target: '.navbar-collapse',
            offset: 195
        
		 });
		 
		
		
		
        /* Scroll To Top */
		
        $(window).scroll(function(){
        if ($(this).scrollTop() >= 500) {
            $('.scroll-to-top').fadeIn();
         } else {
            $('.scroll-to-top').fadeOut();
         }
	   });
	
	
	    $('.scroll-to-top').click(function(){
		  $('html, body').animate({scrollTop : 0},800);
		  return false;
	    });
		
		
		
		
        /* Typed.js */
		
        $(window).load(function(){
        $(".typing").typed({
            strings: ["My name is MSS iThinK", "Yes!! i do analytics for your Data!!", "Choose a file and 'Analyze' it"],    /* You can change the home section typing text from
	                                                                                            here and do not use "&" use "and" */
            typeSpeed: 50
          });
         });
        
         $(window).load(function(){
        $(".loading").typed({
            strings: ["Please wait while analyzing your data","Please wait while analyzing your data","Please wait while analyzing your data","Please wait while analyzing your data","Initializing ApacheSpark......||||", "Creating a SparkContext(sc) ...!", "Deploying the data into Possible Clusters","Converting data into resilient distributed dataset (RDD)","Transforming dataset into Parallelized Connections"],    /* You can change the home section typing text from
                                                                                              here and do not use "&" use "and" */
            typeSpeed: 40
          });
         });

          $(window).load(function(){
        $(".index2").typed({
            strings: ["Choose a field on which you need to make analysis" ],    /* You can change the home section typing text from
                                                                                              here and do not use "&" use "and" */
            typeSpeed: 0
          });
         });
		 
        /* Parallax Background */

        $(window).stellar({
            responsive: true,
            horizontalScrolling: false,
            hideDistantElements: false,
            horizontalOffset: 0,
            verticalOffset: 0,
        });

        
		
		
        /* Portfolio Filtering */

        $('.portfolio-inner').mixItUp();


       
        /* Magnific Popup */

        $('.portfolio-popup').magnificPopup({
            type: 'image',
			
            gallery: { enabled: true },
			zoom: { enabled: true,
			        duration: 500
					
          },
		  
         image:{
               markup: '<div class="mfp-figure portfolio-pop-up">'+
               '<div class="mfp-close"></div>'+
               '<div class="mfp-img"></div>'+
               '<div class="mfp-bottom-bar portfolio_title">'+
               '<div class="mfp-title"></div>'+
               '<div class="mfp-counter"></div>'+
               '</div>'+
               '</div>',

               titleSrc:function(item){
                return item.el.attr('title');
              }
            }
		  
		  
          });

       
	   
		 
        /* Testimonial Carousel/Slider */

        $(".testimonial-carousel-list").owlCarousel({
            items: 1,
            autoPlay: true,
            stopOnHover: false,
            navigation: true,
            navigationText: ["<i class='fa fa-long-arrow-left fa-2x owl-navi'></i>", "<i class='fa fa-long-arrow-right fa-2x owl-navi'></i>"],
            itemsDesktop: [1199, 1],
            itemsDesktopSmall: [980, 1],
            itemsTablet: [768, 1],
            itemsTabletSmall: false,
            itemsMobile: [479, 1],
            autoHeight: true,
            pagination: false,
            transitionStyle : "backSlide"
        });
		
		
		
		
        /* Statistics Counter */
		
        $('.statistics').appear(function() {
           var counter = $(this).find('.statistics-count');
           var toCount = counter.data('count');
      
           $(counter).countTo({
           from: 0,
           to: toCount,
           speed: 5000,
           refreshInterval: 50
           })
           });
		   
		  
         
         /* Google Map */
		 
         $('#my-address').gMap({
            zoom: 5,
            scrollwheel: true,
            maptype: 'ROADMAP',
            markers:[
            {
            address: "New York",  /* You can change your address from here */
            html: "<b>Address</b>: <br> Area-2, Rose Area, New York, U.S.A.",   /* You can change display address text from here */
            popup: true
            }
            ]
            });
              
		   
            });

   })(jQuery);