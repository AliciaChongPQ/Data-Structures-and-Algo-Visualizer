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
            
            text = Text(str(self.nums[0]))
            rect = Rectangle(height=0.5, width=text.width)
            mini_group = VGroup(rect,text).move_to(LEFT*5)
            self.group.add(mini_group)
            prev = mini_group
            for num in self.nums[1:]:
                text = Text(str(num))
                rect = Rectangle(height=0.5,  width=text.width)
                mini_group = VGroup(rect,text).next_to(prev, RIGHT, buff=0.2)
                self.group.add(mini_group)
                prev = mini_group
            
            # prev = self.play(Write(self.group[0].move_to(LEFT*5)))
            # for g in self.group:
            #     self.play(Write(g),run_time=0.3)
            self.play([Write(g) for g in self.group], run_time = 2)
        

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
                    self.play(FadeOut(arrow), run_time = 0.3)
                    return index,group
            error_msg = Text(f"{target} not found").move_to(arrow, UP*5)
            self.play(Write(error_msg), arrow.animate.shift(RIGHT),run_time=0.5)
            self.wait(1)
            self.play(FadeOut(arrow,error_msg), run_time = 0.3)
            return None,None
        
        def delete(target:int):
            index , group = search(target)

            if index is not None:
                
                self.play(FadeOut(group))
                animations = [ self.group[i].animate.move_to(self.group[i - 1], RIGHT)
                                for i in range(index + 1, len(self.group))]
                if len(animations):
                    self.play(*animations, run_time = 0.5)
                    
                self.group.remove(group)
                self.nums.remove(target)
            
        # def insert(num: int,index:int):
        #     temp_group = VGroup()
        #     arrow = Arrow(start=UP * 0.2, end=DOWN, buff=0.1)
        #     text = Text("0") 
        #     text.next_to(arrow, UP)
        #     mini_group = VGroup(arrow, text)
        #     mini_group.next_to(self.group[0], UP)
        #     self.add(mini_group) 
        #     prev = self.group[0]
        #     for i in range(index + 1):
        #         self.play(mini_group.animate.next_to(self.group[i], UP), run_time=0.5)
        #         temp_group.add(self.group[i].next_to(prev, RIGHT, buff=0.2))

        #         new_text = Text(str(i)).move_to(text.get_center())
        #         self.play(ReplacementTransform(text, new_text), run_time=0.2)
        #         text = new_text  
        #         prev = self.group[i]
            
            
        #     new_num = Text(str(num))
        #     new_rect = Rectangle(height=0.5, width=new_num.width)
        #     new_node = VGroup(new_num, new_rect).next_to(self.group[index - 1], RIGHT, buff = 0.2)
        #     prev = new_node
        #     # self.group.insert(index, new_node)
        #     temp_group.add(new_node)

        #     # self.play(Write(new_node))
        #     # animate = [self.group[i].animate.move_to(self.group[i - 1], RIGHT) for i in range(index +1, len(self.group))]
        #     # if len(animate):
        #     #     self.play(*animate, run_time = 0.5)
            
        #     for i in range(index, len(self.nums)):
        #         temp_group.add(self.group[i].next_to(prev, RIGHT, buff=0.2))
        #         prev = self.group[i]
            
        #     self.remove(self.group)
        #     self.group = temp_group
        #     self.play([Write(g) for g in self.group], run_time = 2)
        
        def insert(num: int, index: int):
            temp_group = VGroup()
            
            # Create arrow and text indicator
            arrow = Arrow(start=UP * 0.2, end=DOWN, buff=0.1)
            text = Text("0")
            text.next_to(arrow, UP)
            mini_group = VGroup(arrow, text)
            mini_group.next_to(self.group[0], UP)
            self.add(mini_group)
            
            # Initial position setup without animation
            for i in range(index + 1):
                # Move mini_group to next target position
                mini_group.next_to(self.group[i], UP)
                
                # Update the displayed index number without animating
                new_text = Text(str(i)).move_to(text.get_center())
                text.become(new_text)
            
            # Create the new node at target index
            new_num = Text(str(num))
            new_rect = Rectangle(height=0.5, width=new_num.width)
            new_node = VGroup(new_num, new_rect)
            # temp_group.add(new_node)
            animation = [self.group[i].animate.shift(RIGHT*2) for i in range(index, len(self.group))]
            self.play(*animation)
            
            # Reposition elements in the temp_group without animations
            if index != 0:
                temp_group.add(self.group[i])
                prev = self.group[i].move_to(LEFT*5)
            elif index == 0:
                temp_group.add(new_node.move_to(LEFT*5))
                prev = new_node
            
            i = 1
            while i <= len(self.group):
                if i < index:
                    temp_group.add(self.group[i].next_to(prev, RIGHT, buff=0.2))
                    prev = self.group[i]
                elif i == index:
                    temp_group.add(new_node.next_to(prev, RIGHT, buff=0.2))
                    prev = new_node
                else:
                    temp_group.add(self.group[i-1].next_to(prev, RIGHT, buff=0.2))
                    prev = self.group[i-1]
                i+=1
            
            # Now add animations only
            animations = [Write(g) for g in temp_group]
            self.play(*animations, run_time=2)
            
            # Update self.group to be the new temp_group
            self.group = temp_group

            
            
            # self.group.submobjects.insert(index, new_node)

            # animations = [self.group[i].animate.move_to(self.group[i - 1], RIGHT)
            #                     for i in range(index + 1, len(self.group))]
            # if len(animations):
            #     self.play(*animations, run_time = 0.5)


            self.wait(5)

        construct_list()
        
        for action in self.action_queue:
            if action[0]=="search":
                text = Text("Search "+str(action[1]))
                text.shift(LEFT*5)
                text.shift(UP*3)
                self.add(text)
                search(action[1])
                
            elif action[0]=="delete":
                text = Text("Delete "+str(action[1]))
                text.shift(LEFT*5)
                text.shift(UP*3)
                self.add(text)
                delete(action[1])
            
            elif action[0]=="insert":
                text = Text("Insert "+str(action[1]))
                text.shift(LEFT*5)
                text.shift(UP*3)
                self.add(text)
                insert(action[1], action[2])
            
            self.remove(text)
    
    def search(self, target : int):
        self.action_queue.append(["search", target])
    
    def delete(self, target : int):\
        self.action_queue.append(["delete", target])

    def insert(self, num:int , index : int):\
        self.action_queue.append(["insert",num, index])
        
