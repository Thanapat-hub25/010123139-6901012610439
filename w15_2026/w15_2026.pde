void setup(){
  size(500,500);
  draw_balloon( 200 , 200 );
  draw_balloon( 400 , 300 );
}
void draw_balloon(int x, int y){
  ellipse(x, y, 100, 100);
  line(x, y+50, x, y+200);
}
