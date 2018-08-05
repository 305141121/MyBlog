
$(function(){
	function displayNone(){
		$(".navigator").nextAll().css("display","none");

	}

	// 顶部导航栏显示
	$("#passages").click(function(){	
		displayNone();	
		$(".passages").fadeIn(200);
		$("#passage").hide();
		$("#passage").nextAll().show();			
	});	
	$("#album").click(function(){
		displayNone();	
		$(".album").fadeIn(200);			
	});	
	$("#about").click(function(){
		displayNone();	
		$.get("/static/about.html", function(html){
			$(".about").html(html)
		})
		$(".about").fadeIn(200);			
	})	

	
	// 调用文章编辑器,引用开源editor.md
	function editMode(){
		$(".passages").fadeOut(100);
		$(".navigator").after('<iframe id="editor" src="/static/editor.html"></iframe>')
		$("iframe").fadeToggle(200);		
	}

	// 进入文章详情页
	function getPassage(){
		var name = $(this).attr("name");
		$.get("/static/posts/"+name+".html", function(html){
			$("#passage").attr("name", name);
			$("#passage").nextAll().fadeOut(200);	
			$("#passage").html(html);
			$("#passage").append('<button class="edit">编辑</button>');		
			$("#passage").fadeIn(200);

			$(".edit").click(function(){
				editMode();
			})
		});
	}
	$(".post-item").click(getPassage);

	// 获取对应页的文章列表
	$(".page-item").click(function(){
		var p = ($(this).html());
		var pageJson = {
			"page": p
		}
		$.post("/blogs/page",
			JSON.stringify(pageJson),
			function(data){
				$(".post-item").remove();
				console.log(data)
				dataJSON = JSON.parse(data)
				for (d in dataJSON){
					
					console.log(d)
					$(".passages ul").append(
						'<li class="post-item" name="'+dataJSON[d]["name"]+'"><a href="#">'+dataJSON[d]["name"]+'</a></li>');
				}
				$(".post-item").click(getPassage);
			});
	});
	

});
