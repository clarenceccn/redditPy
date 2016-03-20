int main(int argc, char *argv[])
{
    // ... // draw our borders
    draw_borders(field); draw_borders(score);
    // simulate the game loop 
    while(1) { // draw to our windows mvwprintw(field, 1, 1, "Field"); mvwprintw(score, 1, 1, "Score"); // refresh each window wrefresh(field); wrefresh(score); } // clean up delwin(field); delwin(score); // ... }