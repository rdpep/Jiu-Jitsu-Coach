class DrillNode:
    '''
    Creation of a node to be used for the drill decision
    tree.
    '''
    def __init__(self, prompt=None, options=None, drills=None):
        self.prompt = prompt
        self.options = options or {}
        self.drills = drills or []

    def is_leaf(self) -> bool:
        '''
        Returns whether current node is a leaf or not.
        Indicated by drills being a present attribute.
        '''
        return bool(self.drills)