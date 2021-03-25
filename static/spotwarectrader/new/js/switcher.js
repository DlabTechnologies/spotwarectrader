	
//=== Switcher panal slide function	=====================//

	jQuery(window).load(function(){
		jQuery('.styleswitcher').animate({
					'left': '-220px'
				});
		jQuery('.switch-btn').addClass('closed');
	});
	
	jQuery(document).ready(function () {		
		jQuery('.switch-btn').on('click', function () {	
			if (jQuery(this).hasClass('open')) {
				jQuery(this).addClass('closed');
				jQuery(this).removeClass('open');
				jQuery('.styleswitcher').animate({
					'left': '-220px'
				});
			} else {
				if (jQuery(this).hasClass('closed')) {
				jQuery(this).addClass('open');
				jQuery(this).removeClass('closed');
				jQuery('.styleswitcher').animate({
					'left': '0'
				});
				}
			}	
		});
	});
	
//=== Switcher panal slide function END	=====================//


//=== Color css change function	=====================//

jQuery( document ).ready(function() {
	
    // Color changer
    jQuery(".skin-1").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-1.css");
		jQuery(".logo-header img").attr("src", "images/logo-1.png");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-1.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-1.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-1.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-1.png");
        return false;
    });
    
    jQuery(".skin-2").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-2.html");
		jQuery(".logo-header img").attr("src", "images/logo-2.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-2.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-2.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-2.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-2.html");
        return false;
    });
    
    jQuery(".skin-3").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-3.html");
		jQuery(".logo-header img").attr("src", "images/logo-3.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-3.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-3.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-3.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-3.html");
        return false;
    });
	
    jQuery(".skin-4").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-4.html");
		jQuery(".logo-header img").attr("src", "images/logo-4.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-4.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-4.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-4.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-4.html");
        return false;
    });
	
    jQuery(".skin-5").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-5.html");
		jQuery(".logo-header img").attr("src", "images/logo-5.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-5.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-5.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-5.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-5.html");
        return false;
    });	
	
    jQuery(".skin-6").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-6.html");
		jQuery(".logo-header img").attr("src", "images/logo-6.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-6.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-6.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-6.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-6.html");
        return false;
    });		
		
    jQuery(".skin-7").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-7.html");
		jQuery(".logo-header img").attr("src", "images/logo-7.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-7.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-7.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-7.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-7.html");
        return false;
    });
	
    jQuery(".skin-8").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-8.html");
		jQuery(".logo-header img").attr("src", "images/logo-8.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-8.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-8.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-8.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-8.html");
        return false;
    });	
	
    jQuery(".skin-9").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-9.html");
		jQuery(".logo-header img").attr("src", "images/logo-9.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-9.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-9.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-9.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-9.html");
        return false;
    });	
	
    jQuery(".skin-10").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-10.html");
		jQuery(".logo-header img").attr("src", "images/logo-10.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-10.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-10.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-10.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-10.html");
        return false;
    });	
	
	    jQuery(".skin-11").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-11.html");
		jQuery(".logo-header img").attr("src", "images/logo-11.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-11.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-11.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-11.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-11.html");
        return false;
    });	
	
	    jQuery(".skin-12").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-12.html");
		jQuery(".logo-header img").attr("src", "images/logo-12.html");
		jQuery(".header-style-3 .logo-header img").attr("src", "images/logo-light-12.html");
		jQuery(".header-style-5 .logo-header img").attr("src", "images/logo-light-12.html");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-light-12.html");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-12.html");
        return false;
    });		
		
		
});


//=== Background image change function	=====================//
jQuery(document).ready(function(){
	
	jQuery('.background-switcher li img').on('click', function(){
	 var imgbg = jQuery(this).attr('rel');
	 
	 //console.<span id="IL_AD2" class="IL_AD">log</span>(imgbg);
	 
	 jQuery('#bg').css({backgroundImage: "url("+imgbg+")"});
	 });

});



//=== Background pattern change function	=====================//
jQuery(document).ready(function(){
	
	jQuery('.pattern-switcher li img').on('click', function(){
	 var imgbg = jQuery(this).attr('rel');
	 
	 //console.<span id="IL_AD2" class="IL_AD">log</span>(imgbg);

	 jQuery('#bg').css({backgroundImage: "url("+imgbg+")"});
	 jQuery("#bg").css( "background-size", "auto")
	 
	 });

});


//=== Layout boxed & fullscreen change function	END=====================//
jQuery(document).ready(function(){
	jQuery('.layout-view li ').on('click', function(){
		jQuery('.layout-view li ').removeClass('active');
		jQuery(this).addClass('active');	
	});
	
	jQuery('.wide-layout').on('click', function() { 
		jQuery("body").addClass('wide-layout')
		jQuery("body").removeClass('boxed')
	});
	
	jQuery('.boxed').on('click', function() { 
		jQuery("body").addClass('boxed')
		jQuery("body").removeClass('wide-layout')
	});
	
});

//=== Nav light & dark change function	END=====================//
jQuery(document).ready(function(){
	
	jQuery('.nav-view li ').on('click', function(){
		jQuery('.nav-view li ').removeClass('active');
		jQuery(this).addClass('active');	
	});
	
	jQuery('.nav-light').on('click', function() { 
		jQuery(".header-nav").addClass('nav-light')
		jQuery(".header-nav").removeClass('nav-dark')
	});
	
	jQuery('.nav-dark').on('click', function() { 
		jQuery(".header-nav").addClass('nav-dark')
		jQuery(".header-nav").removeClass('nav-light')
	});
	
});


//=== Nav light & dark change function	END=====================//
jQuery(document).ready(function(){
	
	jQuery('.nav-width li ').on('click', function(){
		jQuery('.nav-width li ').removeClass('active');
		jQuery(this).addClass('active');	
	});
	
	jQuery('.nav-wide').on('click', function() { 
		jQuery(".site-header").addClass('nav-wide')
		jQuery(".site-header").removeClass('nav-boxed')
	});
	
	jQuery('.nav-boxed').on('click', function() { 
		jQuery(".site-header").addClass('nav-boxed')
		jQuery(".site-header").removeClass('nav-wide')
	});
	
});



//=== Nav light & dark change function	END=====================//
jQuery(document).ready(function(){
	
	jQuery('.header-view li ').on('click', function(){
		jQuery('.header-view li ').removeClass('active');
		jQuery(this).addClass('active');	
	});
	
	jQuery('.header-fixed').on('click', function() { 
		jQuery(".main-bar-wraper").addClass('sticky-header')
		jQuery(".main-bar-wraper").removeClass('sticky-no')
	});
	
	jQuery('.header-static').on('click', function() { 
		jQuery(".main-bar-wraper").addClass('sticky-no')
		jQuery(".main-bar-wraper").removeClass('sticky-header')
	});

});

