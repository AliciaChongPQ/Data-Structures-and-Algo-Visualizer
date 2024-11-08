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
            arrow = Arrow(start=UP*0.2, end=DOWN, buff=0.1, color = PURE_RED)
            arrow.next_to(self.group[0], UP)
            # for index, group
            for index,group in enumerate(self.group):
                self.play(arrow.animate.next_to(group, UP),run_time=0.5)
                if self.nums[index] == target:
                    arrow.color = 'PURE_GREEN'
                    self.play(arrow.animate.next_to(group, UP),run_time=0.5)
                    self.wait(1)
                    self.play(FadeOut(arrow), run_time = 0.3)
                    return index,group
            return None,None
        
        def delete(target:int):
            index , group = search(target)

            if index is not None:
                
                self.play(FadeOut(group))
                animations = [ self.group[i].animate.move_to(self.group[i - 1], RIGHT)
                                for i in range(index + 1, len(self.group))]
                self.play(*animations, run_time = 0.5)
                    
                self.group.remove(group)
                self.nums.remove(target)
        construct_list()
        
        for action in self.action_queue:
            if action.startswith("search"):
                text = Text("Search "+action[6:])
                text.shift(LEFT*5)
                text.shift(UP*3)
                self.add(text)
                search(int(action[6:]))
                
            elif action.startswith("delete"):
                text = Text("Delete "+action[6:])
                text.shift(LEFT*5)
                text.shift(UP*3)
                self.add(text)
                delete(int(action[6:]))
                self.remove(self.group)
                self.add(self.group)
            
            self.remove(text)
    
    def search(self, target : int):
        self.action_queue.append("search"+str(target))
    
    def delete(self, target : int):\
        self.action_queue.append("delete"+str(target))
        
