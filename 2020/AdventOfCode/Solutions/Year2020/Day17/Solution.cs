using System;
using System.Collections.Generic;
using System.Text;

namespace AdventOfCode.Solutions.Year2020
{

    class Day17 : ASolution
    {
        char[,,,] grid;
        bool[,,,] changes;
        string[] input;

        public Day17() : base(17, 2020, "")
        {
            grid = new char[30,30,30,30];
            changes = new bool[30,30,30,30];
            input = Input.SplitByNewline();
            //input = new string[] {".#.", "..#", "###"};
            for (int x = 0; x < grid.GetLength(1); x++)
            {
                for (int y = 0; y < grid.GetLength(0); y++)
                {
                    for (int z = 0; z < grid.GetLength(2); z++)
                    {
                        for (int w = 0; w < grid.GetLength(3); w++)
                        {
                            grid[x,y,z,w] = '.';
                        }
                    }
                }
            } 
            for (int x = 0; x < input[0].Length; x++)
            {
                for (int y = 0; y < input.Length; y++)
                {
                    grid[15 + x, 15 + y, 15, 15] = input[x][y];
                }
            }
        }

        protected override string SolvePartOne()
        {
            for (int i = 0; i < 6; i++)
            {
                SolveCycle();
            }
            int count = 0;
            for (int x = 0; x < grid.GetLength(1); x++)
            {
                for (int y = 0; y < grid.GetLength(0); y++)
                {
                    for (int z = 0; z < grid.GetLength(2); z++)
                    {
                        for (int w = 0; w < grid.GetLength(3); w++)
                        {
                            if (grid[x,y,z,w] == '#')
                            {
                                count++;
                            }
                        }
                    }
                }
            } 
            return count.ToString();
        }

        void SolveCycle()
        {
            for (int i = 0; i < changes.GetLength(0); i++)
            {
                for (int j = 0; j < changes.GetLength(1); j++)
                {
                    for (int k = 0; k < changes.GetLength(2); k++)
                    {
                        for (int l = 0; l < changes.GetLength(2); l++)
                            changes[i,j,k, l] = false;
                    }
                }
            } 

            for (int x = 1; x < grid.GetLength(1) - 1; x++)
            {
                for (int y = 1; y < grid.GetLength(0) - 1; y++)
                {
                    for (int z = 1; z < grid.GetLength(2) - 1; z++)
                    {
                        for (int w = 1; w < grid.GetLength(3) - 1; w++)
                        {
                            int count = ActiveNeighbors(x, y, z, w);
                            if (count == 3 && grid[x,y,z,w] == '.')
                            {
                                changes[x,y,z,w] = true;
                            }
                            else if ((count < 2 || count > 3) && grid[x,y,z,w] == '#')
                            {
                                changes[x,y,z,w] = true;
                            }
                        }
                    }
                }
            }

            for (int x = 0; x < changes.GetLength(1); x++)
            {
                for (int y = 0; y < changes.GetLength(0); y++)
                {
                    for (int z = 0; z < changes.GetLength(2); z++)
                    {
                        for (int w = 0; w < changes.GetLength(3); w++)
                        {
                            if (changes[x,y,z,w] && grid[x,y,z,w] == '#')
                            {
                                grid[x,y,z,w] = '.';
                            }
                            else if (changes[x,y,z,w] && grid[x,y,z,w] == '.')
                            {
                                grid[x,y,z,w] = '#';
                            }
                        }    
                    }
                }
            } 
        }

        int ActiveNeighbors(int x, int y, int z, int w)
        {
            int count = 0;

            for (int i = -1; i <= 1; i++)
            {
                for (int j = -1; j <= 1; j++)
                {
                    for (int k = -1; k <= 1; k++)
                    {
                        for (int l = -1; l <= 1; l++)
                        {
                            if (i == 0 && j == 0 && k == 0 && l == 0)
                            {
                                continue;
                            }
                            else
                            {
                                if (grid[x + i, y + j, z + k, w + l] == '#')
                                {
                                    count++;
                                }
                            }
                        }                   
                    }
                }
            }
            return count;
        }

        protected override string SolvePartTwo()
        {
            return null;
        }
    }
}
