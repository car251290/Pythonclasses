
def triplets(a, b, c):
    """
    Core triplets algorithm - counts triplets where a[i] ≤ b[j] ≤ c[k]
    Time complexity: O(n + m + p) where n, m, p are lengths of arrays
    """
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    ai = bi = ci = 0
    ans = 0
    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        ans += ai * ci
        bi += 1
    return ans


def geometry():
    """
    Apply triplets algorithm to various geometric problems in Python
    """
    
    def count_valid_triangles(side_set_a, side_set_b, side_set_c):
        """
        PRACTICAL GEOMETRY: Count valid triangles from three sets of side lengths.
        
        Python Application: Building/Architecture validation, 3D modeling, game development
        Real use case: Given materials of different lengths, how many triangular structures can we build?
        """
        print("🔺 TRIANGLE FORMATION ANALYSIS:")
        print(f"Available sides A: {side_set_a} (shortest sides)")
        print(f"Available sides B: {side_set_b} (medium sides)") 
        print(f"Available sides C: {side_set_c} (longest sides)")
        
        # Step 1: Count all ordered combinations (a ≤ b ≤ c)
        ordered_count = triplets(side_set_a, side_set_b, side_set_c)
        print(f"Total ordered combinations: {ordered_count}")
        
        # Step 2: Apply triangle inequality for valid triangles
        import itertools
        valid_triangles = []
        a_sorted = sorted(set(side_set_a))
        b_sorted = sorted(set(side_set_b))
        c_sorted = sorted(set(side_set_c))
        
        for a in a_sorted:
            for b in b_sorted:
                if b >= a:  # Maintain order a ≤ b
                    for c in c_sorted:
                        if c >= b:  # Maintain order b ≤ c
                            # Triangle inequality: sum of any two sides > third side
                            if a + b > c and a + c > b and b + c > a:
                                valid_triangles.append((a, b, c))
                                
                                # Calculate triangle properties
                                perimeter = a + b + c
                                # Heron's formula for area
                                s = perimeter / 2
                                area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
                                
                                print(f"  ✓ Triangle({a}, {b}, {c}) - Perimeter: {perimeter:.1f}, Area: {area:.2f}")
        
        print(f"Valid triangles found: {len(valid_triangles)}")
        return len(valid_triangles)
    
    def count_coordinate_points(x_coords, y_coords, z_coords):
        """
        PRACTICAL GEOMETRY: 3D coordinate analysis for ascending paths.
        
        Python Application: Pathfinding algorithms, 3D graphics, robotics navigation
        Real use case: Count valid paths where robot moves only in positive directions
        """
        print("\n📍 3D ASCENDING PATH ANALYSIS:")
        print(f"X positions: {x_coords}")
        print(f"Y positions: {y_coords}")
        print(f"Z positions: {z_coords}")
        
        count = triplets(x_coords, y_coords, z_coords)
        
        # Show actual coordinate combinations
        x_sorted = sorted(set(x_coords))
        y_sorted = sorted(set(y_coords))
        z_sorted = sorted(set(z_coords))
        
        valid_paths = []
        for x in x_sorted:
            for y in y_sorted:
                if y >= x:
                    for z in z_sorted:
                        if z >= y:
                            valid_paths.append((x, y, z))
                            # Calculate distance from origin
                            distance = (x**2 + y**2 + z**2) ** 0.5
                            print(f"  ✓ Path: ({x}, {y}, {z}) - Distance from origin: {distance:.2f}")
        
        print(f"Total ascending paths: {count}")
        return count
    
    def count_distance_relationships(dist_ab, dist_bc, dist_ca):
        """
        Count valid distance triplets for three points A, B, C.
        Useful for analyzing geometric configurations.
        """
        print("\n📏 Distance Relationship Problem:")
        print(f"Distances A-B: {dist_ab}")
        print(f"Distances B-C: {dist_bc}")
        print(f"Distances C-A: {dist_ca}")
        
        count = triplets(dist_ab, dist_bc, dist_ca)
        print(f"Valid distance triplets (AB≤BC≤CA): {count}")
        return count
    
    def count_angle_triplets(angles_a, angles_b, angles_c):
        """
        Count angle triplets for triangles where angle_a ≤ angle_b ≤ angle_c.
        Useful for classifying triangle types.
        """
        print("\n📐 Triangle Angle Problem:")
        print(f"Angle set A: {angles_a}")
        print(f"Angle set B: {angles_b}")
        print(f"Angle set C: {angles_c}")
        
        # Filter for valid triangle angles (sum should be close to 180°)
        valid_angle_triplets = 0
        a_sorted = sorted(set(angles_a))
        b_sorted = sorted(set(angles_b))
        c_sorted = sorted(set(angles_c))
        
        for a in a_sorted:
            for b in b_sorted:
                if b >= a:
                    for c in c_sorted:
                        if c >= b and abs((a + b + c) - 180) < 1:  # Sum ≈ 180°
                            valid_angle_triplets += 1
        
        count = triplets(angles_a, angles_b, angles_c)
        print(f"Ordered angle triplets (a≤b≤c): {count}")
        print(f"Valid triangle angles (sum≈180°): {valid_angle_triplets}")
        return valid_angle_triplets
    
    def count_building_heights(low_buildings, mid_buildings, tall_buildings):
        """
        PRACTICAL GEOMETRY: City planning and skyline analysis.
        
        Python Application: Urban planning, architecture, zoning regulations
        Real use case: Count valid building height combinations for city blocks
        """
        print("\n🏗️ CITY SKYLINE PLANNING:")
        print(f"Low buildings: {low_buildings} meters")
        print(f"Mid buildings: {mid_buildings} meters")
        print(f"Tall buildings: {tall_buildings} meters")
        
        count = triplets(low_buildings, mid_buildings, tall_buildings)
        
        # Calculate shadow analysis and visual impact
        low_sorted = sorted(set(low_buildings))
        mid_sorted = sorted(set(mid_buildings))
        tall_sorted = sorted(set(tall_buildings))
        
        valid_combinations = []
        for low in low_sorted:
            for mid in mid_sorted:
                if mid >= low:
                    for tall in tall_sorted:
                        if tall >= mid:
                            valid_combinations.append((low, mid, tall))
                            
                            # Calculate visual progression ratio
                            progression_ratio = tall / low if low > 0 else float('inf')
                            total_height = low + mid + tall
                            
                            print(f"  ✓ Heights: {low}m → {mid}m → {tall}m | "
                                  f"Ratio: {progression_ratio:.1f}x | Total: {total_height}m")
        
        print(f"Valid building combinations: {count}")
        return count
    
    def analyze_geometric_shapes(radii, heights, volumes):
        """
        PRACTICAL GEOMETRY: Cylinder and cone analysis for manufacturing.
        
        Python Application: 3D printing, manufacturing, container design
        Real use case: Optimize container shapes for storage efficiency
        """
        print("\n🎯 GEOMETRIC SHAPE OPTIMIZATION:")
        print(f"Radii: {radii} units")
        print(f"Heights: {heights} units")
        print(f"Volumes: {volumes} cubic units")
        
        count = triplets(radii, heights, volumes)
        
        # Calculate actual geometric properties
        import math
        r_sorted = sorted(set(radii))
        h_sorted = sorted(set(heights))
        v_sorted = sorted(set(volumes))
        
        for r in r_sorted:
            for h in h_sorted:
                if h >= r:  # Practical constraint: height ≥ radius
                    for v in v_sorted:
                        # Calculate cylinder volume: V = πr²h
                        cylinder_volume = math.pi * r**2 * h
                        if v >= cylinder_volume * 0.8:  # Allow some tolerance
                            surface_area = 2 * math.pi * r * (r + h)
                            efficiency = v / surface_area  # Volume to surface ratio
                            
                            print(f"  ✓ Cylinder: r={r}, h={h}, V={v:.1f} | "
                                  f"Calculated V={cylinder_volume:.1f} | "
                                  f"Efficiency={efficiency:.2f}")
        
        print(f"Valid shape combinations: {count}")
        return count
    
    # Run geometric examples
    print("=" * 50)
    print("🔢 GEOMETRIC APPLICATIONS OF TRIPLETS ALGORITHM")
    print("=" * 50)
    
    # Example 1: Triangle sides
    triangle_count = count_valid_triangles(
        [3, 4, 5, 6],      # Possible side lengths for side A
        [4, 5, 6, 7, 8],   # Possible side lengths for side B  
        [5, 6, 7, 8, 9, 10] # Possible side lengths for side C
    )
    
    # Example 2: 3D coordinates
    coord_count = count_coordinate_points(
        [1, 2, 3, 4],      # X coordinates
        [2, 3, 4, 5, 6],   # Y coordinates
        [4, 5, 6, 7, 8, 9] # Z coordinates
    )
    
    # Example 3: Distance relationships
    distance_count = count_distance_relationships(
        [1, 2, 3],         # Distance AB
        [2, 3, 4, 5],      # Distance BC
        [3, 4, 5, 6, 7]    # Distance CA
    )
    
    # Example 4: Triangle angles
    angle_count = count_angle_triplets(
        [30, 45, 60],      # Possible angles A
        [45, 60, 90],      # Possible angles B
        [60, 90, 120]      # Possible angles C
    )
    
    # Example 5: Building height analysis
    building_count = count_building_heights(
        [10, 15, 20],      # Low buildings (meters)
        [25, 30, 35, 40],  # Mid buildings (meters)
        [50, 60, 70, 80]   # Tall buildings (meters)
    )
    
    # Example 6: Geometric shape optimization
    shape_count = analyze_geometric_shapes(
        [1, 2, 3],         # Radii
        [2, 3, 4, 5],      # Heights
        [10, 20, 30, 40, 50] # Volumes
    )
    
    print("\n" + "=" * 50)
    print("📊 SUMMARY OF RESULTS:")
    print("=" * 50)
    return {
        'triangles': triangle_count,
        'coordinates': coord_count,
        'distances': distance_count,
        'angles': angle_count,
        'buildings': building_count,
        'shapes': shape_count
    }

# Test the geometric applications
if __name__ == "__main__":
    results = geometry()
    
    print(f"🔺 Valid triangles found: {results['triangles']}")
    print(f"📍 Coordinate triplets: {results['coordinates']}")
    print(f"📏 Distance relationships: {results['distances']}")
    print(f"📐 Valid angle combinations: {results['angles']}")
    print(f"🏗️ Building combinations: {results['buildings']}")
    print(f"🎯 Shape optimizations: {results['shapes']}")
    
    print(f"\n� Total geometric relationships analyzed: {sum(results.values())}")
    print("\n💡 PYTHON APPLICATIONS:")
    print("  • Architecture & Urban Planning")
    print("  • 3D Graphics & Game Development") 
    print("  • Manufacturing & 3D Printing")
    print("  • Robotics & Path Planning")
    print("  • Engineering Design Validation")
