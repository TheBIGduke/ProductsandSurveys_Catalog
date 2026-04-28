class MockRepository:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self._categories = [{"id": 1, "name": "Robotics"}, {"id": 2, "name": "3D Prints"}]
        self._products = [
            {"id": 10, "name": "Robot Arm v1", "price": 1500.0, "desc": "6-DOF manipulator"},
            {"id": 20, "name": "Custom Gear", "price": 45.0, "desc": "ASA 3D Printed Gear"}
        ]
        self._junction = [{"p_id": 10, "c_id": 1}, {"p_id": 20, "c_id": 2}]
        self._media = [
            {"p_id": 10, "filename": "robot_arm_main.png", "is_primary": True, "pos": 1},
            {"p_id": 20, "filename": "gear_top.jpg", "is_primary": True, "pos": 1}
        ]

    def get_categories(self):
        return self._categories

    def get_products(self, c_id: int = None):
        results = []
        for p in self._products:
            c_ids = [j["c_id"] for j in self._junction if j["p_id"] == p["id"]]
            if c_id and int(c_id) not in c_ids: 
                continue

            cat_names = [c["name"] for c in self._categories if c["id"] in c_ids]
            p_media = [
                {"media_url": f"{self.base_url}/{m['filename']}", "is_primary": m['is_primary'], "pos": m['pos']}
                for m in self._media if m["p_id"] == p["id"]
            ]

            primary = next((m["media_url"] for m in p_media if m["is_primary"]), None)

            results.append({
                **p,
                "categories": cat_names,
                "media": p_media,
                "primary_image": primary,
                "description": p["desc"]
            })
        return results

class SQLRepository:
    def __init__(self, db_path:str, base_url:str):
        self.db_path = db_path
        self.base_url = base_url
    # Future SQLAlchemy queries...
