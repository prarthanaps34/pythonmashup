blog_views = [150,800,2500,600,1200,450,3000];
total_views=0;
no_of_post_trending=0;

for x in blog_views:
    if x >1000:
        print(x,":trending")
        no_of_post_trending +=1
    elif 500< x <1000:
        print(x,":average")
    elif x <500:
        print(x,":low traffic")
    total_views += x
print(total_views,":total number of views")
print(no_of_post_trending,":no of posts trending")
    