/*!
 * quilt.js
 * Used for project site and js file example, but NOT needed to use quilt
 * Copyright 2015 Timothy Davenport; Licensed MIT
 */
$(document).ready(function(){

    /* create Bloodhound searching object */
    var word_search = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('val'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        limit: 10,
        prefetch: { url: pagevars["relativepath"]+'search.json' }
    });

    /* create typeahead searching input */
    word_search.initialize();
    $('.search .typeahead').typeahead(null, {
        name: 'word_search',
        displayKey: 'val',
        source: word_search.ttAdapter(),
        templates: {
            empty: [
                '<div class="empty-message">',
                'hmm... that word doesn\'t seem to be in any page',
                '</div>'
            ].join('\n'),
            suggestion: function(datum){
                return '<p><strong>'+datum.val+'</strong><br><small><a class="text-muted" href="'+datum.url+'">'+datum.url+'</a></small></p>';
            }
        }
    });
    /* if clicked go to that page */
    $('.search').bind('typeahead:selected', function(obj, datum, name) {
        window.location = datum.url
    });






    /*! smooth scrolling by CSS-Tricks, https://css-tricks.com/snippets/jquery/smooth-scrolling/ */
    $(function() {
        $('a[href*=#]:not([href=#])').click(function() {
            if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    });
});
