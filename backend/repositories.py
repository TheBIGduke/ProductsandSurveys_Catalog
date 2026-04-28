class MockRepository:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self._categories = [{"id": 1, "name": "Robotics"}, {"id": 2, "name": "3D Prints"}]
        self._products = [
            {"id": 101, "name": "Robot Arm v1", "price": 12500.0, "desc": "6-DOF manipulator for small payloads"},
            {"id": 102, "name": "Custom Gear Set", "price": 450.0, "desc": "High-torque ASA printed gears"}
        ]
        self._junction = [{"p_id": 101, "c_id": 1}, {"p_id": 102, "c_id": 2}]
        self._media = [
            {"product_id": 101, "filename": "robot_arm.jpg", "is_primary": True},
            {"product_id": 102, "filename": "gears.png", "is_primary": True}
        ]

    def get_categories(self):
        return self._categories

    def get_products(self, category_id: int = None):
        results = []
        for p in self._products:
            c_ids = [j["c_id"] for j in self._junction if j["p_id"] == p["id"]]
            if category_id and int(category_id) not in c_ids:
                continue
            
            cat_names = [c["name"] for c in self._categories if c["id"] in c_ids]
            p_media = [{"media_url": f"{self.base_url}/{m['filename']}", "is_primary": m['is_primary'], "position": 1} 
                       for m in self._media if m["product_id"] == p["id"]]
            
            primary = next((m["media_url"] for m in p_media if m["is_primary"]), None)

            results.append({
                **p, "categories": cat_names, "media": p_media, "primary_image": primary, "description": p.get("desc")
            })
        return results

class SQLRepository:
    def __init__(self, db_path: str, base_url: str):
        self.db_path = db_path
        self.base_url = base_url