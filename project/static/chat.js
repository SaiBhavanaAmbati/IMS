
    $('#btn-chat').bind('click', function() {
        l = document.createElement("LI")
        input = $('#btn-input').val();
        r1 = /ideas similar to/
        r2 = /works relevant to/
        s1 = "ideas similar to neural"
        console.log(s1.replace(r1,''))
        if(input){
            if(input.search(r2) == 0){
                $('.chat').append('<li class="right clearfix"><span class="chat-img pull-right"><img src="http://placehold.it/50/FA6F57/fff&text=ME" alt="User Avatar" class="img-circle" /></span><div class="chat-body clearfix"><div class="header"><strong class="pull-right primary-font">Me</strong></div><p>' +input+'</p></div></li>');
                $('#btn-input').val('');
                
                res = input.replace(r2,'')
                output = $('<div>')

                $.ajax({
                url: '/fetch_relevant_info',
                data: {idea : res},
                type: 'GET',
                success: function(response) {
                    jresponse = JSON.parse(response)
                    console.log(jresponse);
                    for (r in jresponse){
                        output.append($('<div>',{text:parseInt(r) + 1 + ". " + "Title : " + jresponse[r]['title']}))
                        output.append($('<a>',{href:jresponse[r]['link'], text:"Link : " + jresponse[r]['link']}))
                    }
                    $('.chat').append('<li class="left clearfix"><span class="chat-img pull-left"><img src="http://placehold.it/50/55C1E7/fff&text=BOT" alt="User Avatar" class="img-circle" /></span><div class="chat-body clearfix"><div class="header"><strong class="primary-font">IdeaBot</strong><small class="text-muted"></div><p>' +output.get(0).outerHTML+'</p></div></li>');
                        
                    },
                })
                
                
                
            }
            
        }
    })

