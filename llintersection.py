class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        nodeA, nodeB = headA, headB
        lenA, lenB = 0, 0
        while nodeA:
            lenA, nodeA = lenA + 1, nodeA.next
        while nodeB:
            lenB, nodeB = lenB + 1, nodeB.next
        nodeA, nodeB = headA, headB
        for _ in range(abs(lenA-lenB)):
            if lenA >= lenB:
                nodeA = nodeA.next
            else:
                nodeB = nodeB.next
        while nodeA != nodeB:
            nodeA, nodeB = nodeA.next, nodeB.next
        return nodeA