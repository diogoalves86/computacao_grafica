boolean mouseEstaNoPonto2 = false;
boolean mouseEstaNoPonto3 = false;

float x1 = 200;
float y1 = 400;
float x2 = 400;
float y2 = 100;
float x3 = 600;
float y3 = 300;
float x4 = 500;
float y4 = 500;

void setup() {
  size (800, 800);
}

void draw() {
  background(#000000);
  
  if(mouseEstaNoPonto2) {
    x2 = mouseX;
    y2 = mouseY;
  }
  else if(mouseEstaNoPonto3) {
    x3 = mouseX;
    y3 = mouseY;
  }
noFill();
beginShape();

  for(float t = 0; t <= 1; t += 0.01) {
    float ax = x1 + t*(x2-x1);
    float ay = y1 + t*(y2-y1);    
    float bx = x2 + t*(x3-x2);
    float by = y2 + t*(y3-y2);    
    float cx = x3 + t*(x4-x3);
    float cy = y3 + t*(y4-y3);    
    float dx = ax + t*(bx-ax);
    float dy = ay + t*(by-ay);    
    float ex = bx + t*(cx-bx);
    float ey = by + t*(cy-by);   
    float fx = dx + t*(ex-dx);
    float fy = dy + t*(ey-dy);

    vertex(fx,fy);
    stroke(#FFFFFF);
    strokeWeight(2);
  }
  endShape();
  
  fill(255, 0, 0);
  circle(x1, y1, 10);
  circle(x2, y2, 10);
  circle(x3, y3, 10);
  circle(x4, y4, 10);
}

void mousePressed() {
    mouseEstaNoPonto2 = dist(x2, y2, mouseX, mouseY) < 10;
    mouseEstaNoPonto3 = dist(x3, y3, mouseX, mouseY) < 10;
}
 
void mouseReleased() {
  mouseEstaNoPonto2 = false;
  mouseEstaNoPonto3 = false;
}
