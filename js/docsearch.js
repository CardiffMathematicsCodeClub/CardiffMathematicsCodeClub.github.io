---
# Thanks to katydecorah.com/code/lunr-and-jekyll/ for details on how to se this up
---

// Tell lunr about which fields we want in the index
var index = lunr(function(){
    this.field("title");
    this.field("content");
    this.ref("id");
});

// Next we need to build the index so we get jekyll to loop over the document
// collection and add each one in turn to the index
{% assign count = 0 %}
{% for doc in site.docs %}

    index.add({
        title: {{doc.title | jsonify}},
        content: {{doc.content | strip_html | jsonify}},
        id: {{count}}
    });

    {% assign count = count | plus: 1 %}

{% endfor %}

// Lunr only returns the index number of the result, so we need to keep track of
// index ourselves
var store = [{% for doc in site.docs %} {
    'title': {{doc.title | jsonify}},
    'link': {{doc.url | jsonify}},
    'excerpt': {{doc.content | strip_html | truncatewords: 20 | jsonify}}
    }{% unless forloop.last %},{% endunless %}{% endfor %}
];

// Finally we need to make the search box useful
$(document).ready(function(){

    $("input#search").on("keyup", function(){
        // "Pick up" the results div
        var results = $("#results");

        // Get the query string and search
        var query = $(this).val();
        var result = index.search(query);

        // Clear the previous results
        results.empty();

        // // Start a list
        results.append("<ul>");

        // // Loop through the results and put them in the result div
        for (item in result) {
            var ref = result[item].ref;

            var resitem = "<a href='" + store[ref].link + "'>"
                   + "<h4>" +  store[ref].title + "</h4>" + "</a>"
                    + "<p>" + store[ref].excerpt + "</p>";

            results.append(resitem);
        }

        // Finish the list
        results.append("</ul>");

        console.log("Searching...");
    });
    //Each time the user types a character
    // $("inupt#search").on("keyup", function() {


    // });
});
