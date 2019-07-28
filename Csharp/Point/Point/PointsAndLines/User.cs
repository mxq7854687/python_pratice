using System;
namespace PointsAndLines
{
    public class Point
    {
        private int x;
        private int y;

        public int X {
            get {
                return x;
            }
            set {
                x = value;
                    }
        }

        public Point()
        {

        }
        public Point(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }
}



