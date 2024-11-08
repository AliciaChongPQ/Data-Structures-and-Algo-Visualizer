from manim import *


class LinkedList(Scene):
    def __init__(self, nums: List[int], **kwargs):
        super().__init__(**kwargs)
        self.nums = nums
        self.group = VGroup()
        self.action_queue = []
        self.action_index = 0
    def construct(self):
        def construct_list():
            rect = Rectangle(height=0.5, width=0.5)
            text = Text(str(self.nums[0]))
            mini_group = VGroup(rect,text).move_to(LEFT*5)
            self.group.add(mini_group)
            prev = mini_group
            for num in self.nums[1:]:
                rect = Rectangle(height=0.5, width=0.5)
                text = Text(str(num))
                mini_group = VGroup(rect,text).next_to(prev, RIGHT, buff=0.2)
                self.group.add(mini_group)
                prev = mini_group
            
            # prev = self.play(Write(self.group[0].move_to(LEFT*5)))
            for g in self.group:
                self.play(Write(g),run_time=0.3)
        

        def show_arrow():
            arrow = Arrow(start=UP*0.2, end=DOWN, buff=0.1)
            arrow.next_to(self.group[0], UP)
            self.add(arrow)
            
            for g in self.group:
                self.play(arrow.animate.next_to(g, UP),run_time=0.3)
        
        def search(target:int):
            text = Text("Search "+str(target))
            text.shift(LEFT*5)
            text.shift(UP*3)
            self.add(text)
            arrow = Arrow(start=UP*0.2, end=DOWN, buff=0.1, color = PURE_RED)
            arrow.next_to(self.group[0], UP)
            for i,g in enumerate(self.group):
                self.play(arrow.animate.next_to(g, UP),run_time=0.5)
                if self.nums[i] == target:
                    arrow.color = 'PURE_GREEN'
                    self.play(arrow.animate.next_to(g, UP),run_time=0.5)
                    self.wait(3)
                    break
                
                
                
                
        
        construct_list()
        
        for action in self.action_queue:
            if action.startswith("search"):
                search(int(action[6:]))
    
    def search(self, target : int):
        self.action_queue.append("search"+str(target))
        
