    function like(id){
        $.ajax({
            type: "GET",
            url: "/memories/like/",
            data: {
                memory_id: id,
            },
            success: function(res) {
                $("#icon_like"+id).removeClass('fa-heart-o'); 
                $("#icon_like"+id).addClass('fa-heart'); 
            }
        });
    }
