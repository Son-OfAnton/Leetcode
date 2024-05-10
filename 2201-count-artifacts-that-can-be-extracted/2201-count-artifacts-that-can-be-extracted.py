class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        pos_to_artifacts = dict() # (x, y) => artifact unique index
        artifacts_to_remaining = dict() # artifact unique index to remaining spots for artifact to dig up
        res = 0
        
        for subgrid_id, artifact in enumerate(artifacts):
            tr, tc, br, bc = artifact
            start, end = (artifact[0], artifact[1]), (artifact[2], artifact[3])
            grid_size = 0
            
            for r in range(tr, br + 1):
                for c in range(tc, bc + 1):
                    pos_to_artifacts[(r,c)] = subgrid_id
                    grid_size += 1
                    
            artifacts_to_remaining[subgrid_id] = grid_size
        
        for r, c in dig:
            if (r, c) not in pos_to_artifacts:
                continue
                
            subgrid_id = pos_to_artifacts[(r,c)]
            artifacts_to_remaining[subgrid_id] = artifacts_to_remaining[subgrid_id] - 1
            
            if artifacts_to_remaining[subgrid_id] == 0:
                res += 1

        return res