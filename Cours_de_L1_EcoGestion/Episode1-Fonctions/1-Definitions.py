from manim import *


class RappelEnsemble(Scene):
    def construct(self):
        listIncl = MathTex(
            r"\mathbb{N}\subset\mathbb{Z}\subset\mathbb{D}\subset\mathbb{Q}\subset\mathbb{R}",
        ).scale(2)
        listIncl.move_to(3 * UP)
        self.play(Write(listIncl), run_time=2)

        self.wait(4)

        defN = MathTex(r"\mathbb{N} = \{0,1,\ldots\}").scale(1.5)
        defN.next_to(listIncl, DOWN)
        self.play(Write(defN), run_time=1)

        self.wait(5)

        defZ = MathTex(r"\mathbb{Z} = \{\ldots,-1,0,1,\ldots\}").scale(1.5)
        defZ.next_to(defN, DOWN)
        self.play(Write(defZ), run_time=1)

        self.wait(5)

        defD = MathTex(
            r"\mathbb{D}",
            r"= \left \{ \dfrac{n}{10^p},n\in\mathbb{Z},p\in\mathbb{N} \right \}",
        ).scale(1.5)
        defD.next_to(defZ, DOWN)
        self.play(Write(defD[0]), run_time=1)
        framebox = SurroundingRectangle(defD[0], buff=0.4)
        self.play(
            Create(framebox),
        )
        self.wait(5)

        self.play(Uncreate(framebox), Write(defD[1]), run_time=1)

        self.wait(5)

        exempleD = MathTex(
            r"\text{Exemple: } 1,75 ", r" = \dfrac{175}{100}", r"= \dfrac{175}{10^2}"
        ).scale(1.5)
        exempleD.next_to(defD, DOWN)
        self.play(Write(exempleD[0]), run_time=1)
        self.wait(2)
        self.play(Write(exempleD[1]), run_time=1)
        self.wait(2)
        self.play(Write(exempleD[2]), run_time=1)
        self.wait(4)

        self.play(
            Unwrite(listIncl, reverse=True),
            Unwrite(defN, reverse=True),
            Unwrite(defZ, reverse=True),
            Unwrite(defD, reverse=True),
            Unwrite(exempleD, reverse=True),
            run_time=1,
        )

        self.wait(1)

        defQ = MathTex(
            r"\mathbb{Q}",
            r"= \left\{\left.{\dfrac {m}{n}}\right|(m,n)\in \mathbb{Z } \times (\mathbb{Z } \setminus \{0\})\right\}",
        ).scale(1.75)
        self.play(Write(defQ[0]),run_time=1)
        self.play(Indicate(defQ[0]),run_time=1)
        
        self.wait(5)

        self.play(Write(defQ[1]), run_time=1)

        self.wait(5)


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

        Total = MathTex(
            r"\text{On notera alors } R = q_1\times p_1 + q_2\times p_2 \text{ le revenu total obtenu.}"
        )
        Everything = VGroup(
            def_of_q1_and_q2,
            def_of_p1_and_p2,
            p1_p2_inQ,
            q1_q2_inZ,
        )
        self.play(
            ReplacementTransform(
                Everything,
                Total,
            ),
            run_time=2,
        )

        self.wait(2)
