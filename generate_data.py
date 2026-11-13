import random
import datetime
import json

STORES = [
    {"store_id": "CH01", "store_name": "Phúc An - Quận 1 (Nguyễn Huệ)", "region": "Miền Nam", "tier": "A", "target_revenue": 2800000000},
    {"store_id": "CH02", "store_name": "Phúc An - Quận 3 (Võ Văn Tần)", "region": "Miền Nam", "tier": "A", "target_revenue": 2400000000},
    {"store_id": "CH03", "store_name": "Phúc An - Quận 7 (Phú Mỹ Hưng)", "region": "Miền Nam", "tier": "A", "target_revenue": 2600000000},
    {"store_id": "CH04", "store_name": "Phúc An - Bình Thạnh (Điện Biên Phủ)", "region": "Miền Nam", "tier": "B", "target_revenue": 1900000000},
    {"store_id": "CH05", "store_name": "Phúc An - Tân Bình (Cộng Hòa)", "region": "Miền Nam", "tier": "B", "target_revenue": 1850000000},
    {"store_id": "CH06", "store_name": "Phúc An - Gò Vấp (Quang Trung)", "region": "Miền Nam", "tier": "B", "target_revenue": 1750000000},
    {"store_id": "CH07", "store_name": "Phúc An - TP. Thủ Đức (Thảo Điền)", "region": "Miền Nam", "tier": "A", "target_revenue": 2500000000},
    {"store_id": "CH08", "store_name": "Phúc An - Quận 10 (Sư Vạn Hạnh)", "region": "Miền Nam", "tier": "B", "target_revenue": 1800000000},
    {"store_id": "CH09", "store_name": "Phúc An - Hoàn Kiếm (Tràng Tiền)", "region": "Miền Bắc", "tier": "A", "target_revenue": 2700000000},
    {"store_id": "CH10", "store_name": "Phúc An - Ba Đình (Liễu Giai)", "region": "Miền Bắc", "tier": "A", "target_revenue": 2300000000},
    {"store_id": "CH11", "store_name": "Phúc An - Cầu Giấy (Xuân Thủy)", "region": "Miền Bắc", "tier": "B", "target_revenue": 1950000000},
    {"store_id": "CH12", "store_name": "Phúc An - Đống Đa (Chùa Bộc)", "region": "Miền Bắc", "tier": "B", "target_revenue": 1850000000},
    {"store_id": "CH13", "store_name": "Phúc An - Hà Đông (Trần Phú)", "region": "Miền Bắc", "tier": "C", "target_revenue": 1400000000},
    {"store_id": "CH14", "store_name": "Phúc An - Long Biên (Nguyễn Văn Cừ)", "region": "Miền Bắc", "tier": "C", "target_revenue": 1350000000},
    {"store_id": "CH15", "store_name": "Phúc An - Hải Châu (Đà Nẵng)", "region": "Miền Trung", "tier": "A", "target_revenue": 2200000000},
    {"store_id": "CH16", "store_name": "Phúc An - Thanh Khê (Đà Nẵng)", "region": "Miền Trung", "tier": "B", "target_revenue": 1600000000},
    {"store_id": "CH17", "store_name": "Phúc An - Nha Trang (Trần Phú)", "region": "Miền Trung", "tier": "B", "target_revenue": 1700000000},
    {"store_id": "CH18", "store_name": "Phúc An - TP. Cần Thơ (30 Tháng 4)", "region": "Miền Nam", "tier": "C", "target_revenue": 1450000000},
]

PRODUCTS = [
    {"sku": "SKU001", "name": "Nồi chiên không dầu 6.5L SmartLock", "category": "Gia dụng", "cost_price": 850000, "sale_price": 1450000},
    {"sku": "SKU002", "name": "Máy xay sinh tố đa năng 3 cối Pro", "category": "Gia dụng", "cost_price": 420000, "sale_price": 790000},
    {"sku": "SKU003", "name": "Robot hút bụi lau nhà RoboSweep X5", "category": "Gia dụng thông minh", "cost_price": 3100000, "sale_price": 5490000},
    {"sku": "SKU004", "name": "Máy lọc không khí Plasma AirClean", "category": "Gia dụng thông minh", "cost_price": 1950000, "sale_price": 3290000},
    {"sku": "SKU005", "name": "Bình giữ nhiệt Inox 316 Cao cấp 1000ml", "category": "Đời sống", "cost_price": 110000, "sale_price": 280000},
    {"sku": "SKU006", "name": "Bàn chải điện Sonic Clean 5 chế độ", "category": "Chăm sóc cá nhân", "cost_price": 190000, "sale_price": 450000},
    {"sku": "SKU007", "name": "Máy sấy tóc ion âm tốc độ cao Pro", "category": "Chăm sóc cá nhân", "cost_price": 380000, "sale_price": 890000},
    {"sku": "SKU008", "name": "Bếp điện từ đơn cảm ứng siêu mỏng", "category": "Gia dụng", "cost_price": 450000, "sale_price": 890000},
    {"sku": "SKU009", "name": "Chảo chống dính tổ ong Ceramic 28cm", "category": "Gia dụng", "cost_price": 160000, "sale_price": 390000},
    {"sku": "SKU010", "name": "Bộ hộp cơm giữ nhiệt văn phòng LockPlus", "category": "Đời sống", "cost_price": 140000, "sale_price": 320000},
    {"sku": "SKU011", "name": "Cân điện tử sức khỏe thông minh Bluetooth", "category": "Chăm sóc cá nhân", "cost_price": 120000, "sale_price": 290000},
    {"sku": "SKU012", "name": "Quạt tháp lọc không khí Ion Tower", "category": "Gia dụng thông minh", "cost_price": 1200000, "sale_price": 2190000},
]

random.seed(42)
total_rows = 60000
current_count = int(total_rows * 0.55)
rows = []
start_cur = datetime.date(2026, 10, 1)
start_cmp = datetime.date(2026, 9, 1)

for i in range(total_rows):
    is_current = (i < current_count)
    if is_current:
        trans_date = start_cur + datetime.timedelta(days=random.randint(0, 30))
        period = "2026-10"
    else:
        trans_date = start_cmp + datetime.timedelta(days=random.randint(0, 29))
        period = "2026-09"

    store = random.choice(STORES)
    prod = random.choice(PRODUCTS)
    qty = random.choices([1, 2, 3, 4, 5], weights=[0.65, 0.20, 0.08, 0.04, 0.03])[0]

    if store["store_id"] in ["CH13", "CH18"]:
        status = random.choices(["Hoàn thành", "Đã hủy", "Đổi trả"], weights=[0.76, 0.12, 0.12])[0]
    elif store["store_id"] in ["CH01", "CH09"]:
        status = random.choices(["Hoàn thành", "Đã hủy", "Đổi trả"], weights=[0.92, 0.04, 0.04])[0]
    else:
        status = random.choices(["Hoàn thành", "Đã hủy", "Đổi trả"], weights=[0.87, 0.07, 0.06])[0]

    unit_price = prod["sale_price"]
    line_amount = qty * unit_price
    raw_qty = qty
    raw_amount = line_amount
    if status == "Đổi trả" and random.random() < 0.5:
        raw_qty = -qty
        raw_amount = -line_amount

    trans_id = f"TXN-{trans_date.strftime('%Y%m')}-{i+1:06d}"
    rows.append({
        "trans_id": trans_id,
        "trans_date": trans_date.strftime("%Y-%m-%d"),
        "period": period,
        "store_id": store["store_id"],
        "store_name": store["store_name"],
        "sku": prod["sku"],
        "product_name": prod["name"],
        "category": prod["category"],
        "quantity": raw_qty,
        "unit_price": unit_price,
        "line_amount": raw_amount,
        "status": status,
        "cost_price": prod["cost_price"]
    })

# Add duplicates
for idx in random.sample(range(len(rows)), 1200):
    rows.append(dict(rows[idx]))

# Process Cleaning
seen_ids = set()
clean_rows = []
dup_count = 0
canceled_count = 0
canceled_val = 0
return_count = 0

for r in rows:
    if r["trans_id"] in seen_ids:
        dup_count += 1
        continue
    seen_ids.add(r["trans_id"])

    if r["status"] == "Đã hủy":
        canceled_count += 1
        canceled_val += abs(r["line_amount"])
        continue

    is_ret = (r["status"] == "Đổi trả")
    if is_ret:
        return_count += 1
        clean_qty = -abs(r["quantity"])
    else:
        clean_qty = abs(r["quantity"])

    net_amt = clean_qty * r["unit_price"]
    cogs = clean_qty * r["cost_price"]
    profit = net_amt - cogs

    clean_rows.append({
        **r,
        "clean_quantity": clean_qty,
        "net_amount": net_amt,
        "total_cogs": cogs,
        "gross_profit": profit
    })

audit = {
    "total_raw": len(rows),
    "total_duplicates_removed": dup_count,
    "total_canceled_removed": canceled_count,
    "total_canceled_value": float(canceled_val),
    "total_returns_standardized": return_count,
    "total_clean_rows": len(clean_rows)
}

store_map_cur = {s["store_id"]: {"rev": 0, "gross_sales": 0, "ret_sales": 0, "cogs": 0, "profit": 0} for s in STORES}
store_map_cmp = {s["store_id"]: {"rev": 0, "profit": 0} for s in STORES}
cat_map = {}

for r in clean_rows:
    sid = r["store_id"]
    amt = r["net_amount"]
    pft = r["gross_profit"]
    cat = r["category"]
    if r["period"] == "2026-10":
        store_map_cur[sid]["rev"] += amt
        store_map_cur[sid]["cogs"] += r["total_cogs"]
        store_map_cur[sid]["profit"] += pft
        if amt > 0:
            store_map_cur[sid]["gross_sales"] += amt
        else:
            store_map_cur[sid]["ret_sales"] += abs(amt)

        k = (sid, cat)
        if k not in cat_map:
            cat_map[k] = {"rev": 0, "profit": 0}
        cat_map[k]["rev"] += amt
        cat_map[k]["profit"] += pft
    else:
        store_map_cmp[sid]["rev"] += amt
        store_map_cmp[sid]["profit"] += pft

reports = []
rankings = []
for s in STORES:
    sid = s["store_id"]
    cur = store_map_cur[sid]
    cmp_ = store_map_cmp[sid]
    tgt = s["target_revenue"]
    kpi = (cur["rev"] / tgt) * 100
    margin = (cur["profit"] / cur["rev"] * 100) if cur["rev"] > 0 else 0
    rev_mom = ((cur["rev"] - cmp_["rev"]) / cmp_["rev"] * 100) if cmp_["rev"] > 0 else 0
    pft_mom = ((cur["profit"] - cmp_["profit"]) / cmp_["profit"] * 100) if cmp_["profit"] > 0 else 0
    ret_rate = (cur["ret_sales"] / cur["gross_sales"] * 100) if cur["gross_sales"] > 0 else 0

    reports.append({
        "store_id": sid,
        "store_name": s["store_name"],
        "region": s["region"],
        "tier": s["tier"],
        "target_revenue": tgt,
        "net_revenue": round(cur["rev"], 0),
        "net_revenue_prev": round(cmp_["rev"], 0),
        "gross_profit": round(cur["profit"], 0),
        "gross_profit_prev": round(cmp_["profit"], 0),
        "kpi_completion_pct": round(kpi, 1),
        "gross_margin_pct": round(margin, 1),
        "revenue_growth_mom": round(rev_mom, 1),
        "profit_growth_mom": round(pft_mom, 1),
        "return_rate_revenue": round(ret_rate, 1)
    })

    anomalies = []
    recs = []
    if rev_mom > 0 and pft_mom < -2:
        anomalies.append(f"⚠️ NGHỊCH LÝ: Doanh thu tăng {rev_mom:.1f}% nhưng Lợi nhuận giảm {pft_mom:.1f}%.")
        recs.append("Kiểm tra rổ hàng: xả hàng khuyến mãi quá đà hoặc cơ cấu mặt hàng margin thấp.")
    if ret_rate >= 8.0:
        anomalies.append(f"🚨 TỶ LỆ TRẢ HÀNG CAO: {ret_rate:.1f}% doanh số bị trừ do trả hàng.")
        recs.append("Rà soát quy trình hướng dẫn khách dùng & bảo quản lô hàng tồn kho.")
    if kpi < 80:
        anomalies.append(f"🔴 BÁO ĐỘNG KPI: Chỉ đạt {kpi:.1f}% mục tiêu tháng.")
        recs.append("Giám đốc vùng cần xuống trực tiếp hỗ trợ, thúc đẩy conversion rate.")
    elif kpi < 90:
        anomalies.append(f"🟡 Chưa đạt chuẩn KPI: Đạt {kpi:.1f}%.")
        recs.append("Bổ sung hoạt động bán hàng cuối tuần, đẩy các mã chủ lực margin cao.")

    kpi_def = max(0, 100 - kpi) * 0.4
    rev_def = max(0, -rev_mom) * 0.25
    pft_def = max(0, -pft_mom) * 0.20
    ret_pen = max(0, ret_rate - 4.0) * 3.5
    score = min(100.0, kpi_def + rev_def + pft_def + ret_pen)

    if score >= 40:
        plevel = "Ưu tiên 1: Hỗ trợ khẩn cấp"
    elif score >= 20:
        plevel = "Ưu tiên 2: Cần can thiệp theo dõi"
    else:
        plevel = "Ưu tiên 3: Vận hành ổn định"
        if not recs:
            recs.append("Duy trì nhịp độ bán hàng hiện tại, phát huy nhóm best-seller.")

    rankings.append({
        "store_id": sid,
        "store_name": s["store_name"],
        "tier": s["tier"],
        "region": s["region"],
        "priority_score": round(score, 1),
        "priority_level": plevel,
        "kpi_completion_pct": round(kpi, 1),
        "net_revenue": round(cur["rev"], 0),
        "gross_profit": round(cur["profit"], 0),
        "revenue_growth_mom": round(rev_mom, 1),
        "profit_growth_mom": round(pft_mom, 1),
        "return_rate_revenue": round(ret_rate, 1),
        "anomalies": anomalies,
        "recommendations": recs
    })

rankings.sort(key=lambda x: x["priority_score"], reverse=True)

cat_list = []
for (sid, cat), val in cat_map.items():
    cat_list.append({
        "store_id": sid,
        "category": cat,
        "cat_revenue": round(val["rev"], 0),
        "cat_profit": round(val["profit"], 0)
    })

bundle = {
    "audit": audit,
    "raw_sample": rows[:20],
    "clean_sample": clean_rows[:20],
    "stores": STORES,
    "products": PRODUCTS,
    "report": reports,
    "ranking": rankings,
    "category_summary": cat_list
}

# Write both data.js and data.json
with open("data.js", "w", encoding="utf-8") as f:
    f.write("const PHUC_AN_DATA = " + json.dumps(bundle, ensure_ascii=False) + ";")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(bundle, f, ensure_ascii=False)

print("Generated data.js and data.json successfully!")

