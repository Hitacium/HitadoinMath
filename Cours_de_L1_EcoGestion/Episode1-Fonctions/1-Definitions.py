from manim import *

class FirstDefinition(Scene):
    def construct(self):
        def_of_q1_and_q2 = MathTex(
            r"\text{On pose } q_1 \text{ et } q_2 \text{ deux biens avec une quantité respective}."
        )  # definition of q1 and q2 a quantity
        def_of_q1_and_q2.move_to(1.5 * UP)
        self.play(Write(def_of_q1_and_q2), run_time=2)

        self.wait(1)

        q1_q2_inZ = MathTex(
            r"(q_1,q_2)\in \mathbb{Z}"
        )  # precise that q1 and q2 are relative numbers
        q1_q2_inZ.next_to(def_of_q1_and_q2, DOWN)
        self.play(Write(q1_q2_inZ), run_time=0.4)

        self.wait(2)

        def_of_p1_and_p2 = MathTex(
            r"\text{On pose aussi } p_1 \text{ et } p_2 \text{ le prix de ces deux biens}."
        )
        self.play(Write(def_of_p1_and_p2), run_time=2)

        self.wait(1)

        p1_p2_inQ = MathTex(
            r"(p_1,p_2)\in \mathbb{Q}"
        )  # precise that q1 and q2 are relative numbers
        p1_p2_inQ.next_to(def_of_p1_and_p2, DOWN)
        self.play(Write(p1_p2_inQ), run_time=0.4)

        self.wait(2)

        Total = MathTex(r"\text{On notera alors } R = q_1\times p_1 + q_2\times p_2 \text{ le revenu total obtenu.}")
        Everything = VGroup(def_of_q1_and_q2, def_of_p1_and_p2, p1_p2_inQ, q1_q2_inZ, )
        self.play(Transform(Everything, Total,), run_time=2)

        self.wait(2)